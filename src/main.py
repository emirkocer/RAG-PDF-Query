from extract import extract_text_from_pdf, chunk_text_into_paragraphs
from vectorize import vectorize_paragraphs
from database import create_chromadb_database, store_into_collection
from query import retrieve_context
import os
import utils as utils
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import openai
from dotenv import load_dotenv
import prompts as prompts
from test_questions import test_questions


def generate_agent_answer(context, system_prompt, question):
    """
    Uses GPT-4 to generate an answer to a question based on provided context.

    Parameters:
    - context (str): Relevant context retrieved from ChromaDB.
    - question (str): The user's question.
    - api_key (str): OpenAI API key.

    Returns:
    - str: The model's generated answer.
    """

    prompt = prompts.get_prompt_plain(context, question)

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "developer", "content": system_prompt}, {"role": "user", "content": prompt}],
        stream=True,
        )
    
    agent_answer = ""
    for chunk in response:
        delta_content = chunk.choices[0].delta.content
        if delta_content:  # Only add non-empty content
            agent_answer += delta_content

    return agent_answer


def main():
    
    # Load the OpenAI API key
    load_dotenv()

    # Path to PDF files
    data_folder = "../data"

    # Chunk into paragraphs and merge all into one
    all_paragraphs = []

    for filename in os.listdir(data_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(data_folder, filename)
            print(f"Processing file: {filename}")

            # Extract text from the PDF
            raw_text = extract_text_from_pdf(filepath)

            # Split the text into paragraphs
            paragraphs = chunk_text_into_paragraphs(raw_text)

            # Add paragraphs to the master list
            all_paragraphs.extend(paragraphs)

    # Generate embeddings
    embeddings = vectorize_paragraphs(all_paragraphs, utils.MODEL)

    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=utils.MODEL) 

    # Check the shape of embeddings
    print(f"Number of embeddings: {len(embeddings)}")
 
    # CHROMADB
    client = chromadb.Client(Settings())

    # Create a new collection
    collection = create_chromadb_database(utils.DATABASE_NAME, sentence_transformer_ef)

    # Store the embeddings into the collection
    store_into_collection(all_paragraphs, embeddings, collection)

    # Retrieve context
    collection = client.get_collection(utils.DATABASE_NAME)
    #collection = client.get_collection(utils.DATABASE_NAME, sentence_transformer_ef)

    # TESTING
    print("Answers for pre-defined questions:\n")
    for i, question in enumerate(test_questions):
        print(f"Question {i+1}: {question}")
        context = retrieve_context(question, collection, 4)
        if not context:
            print("The given documents do not provide enough context for this question.\n")
            continue
        answer = generate_agent_answer(context, prompts.system_prompt, question)
        print(f"Answer:\n{answer}\n{'-'*80}")


    # Step 2: Enable user to ask new questions
    print("Please ask questions about the documents (type 'exit' to exit):\n")
    while True:
        user_question = input("Your question: ")
        if user_question.lower() == "exit":
            print("Thank you !")
            break
        if not user_question.strip():
            print("Please enter a valid question.")
            continue
        context = retrieve_context(user_question, collection, 4)
        if not context:
            print("The documents do not contain sufficient information.\n")
            continue
        answer = generate_agent_answer(context, prompts.system_prompt, user_question)
        print(f"Answer:\n{answer}\n{'-'*80}")
    
if __name__ == "__main__":
    main()