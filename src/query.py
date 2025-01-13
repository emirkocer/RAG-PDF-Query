import os
import utils

# Function to retrieve chunks from ChromaDB relevant to the user's query
def retrieve_context(question, collection, top_k):
    """
    Retrieves the most relevant chunks from ChromaDB.

    Parameters:
    - question (str): The user's query.
    - collection: The ChromaDB collection object.
    - top_k (int): Number of top results to retrieve.

    Returns:
    - str: Combined context of the retrieved chunks.
    """
    results = collection.query(
        query_texts=[question],
        n_results=top_k,
    )

    ### TODO: filter out results with low similarity scores

    context = "\n".join(results["documents"][0])
    
    return context