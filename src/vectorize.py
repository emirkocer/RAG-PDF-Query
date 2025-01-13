from sentence_transformers import SentenceTransformer

def vectorize_paragraphs(paragraphs, model_name):
    """
    Generates embeddings for a list of paragraphs using Sentence Transformers.

    Parameters:
    - paragraphs (List[str]): List of text paragraphs.
    - model_name (str): Name of the pre-trained embedding model.

    Returns:
    - List[ndarray]: List of embeddings.
    """
    print("Initializing embedding model...")
    model = SentenceTransformer(model_name)

    print(f"Embedding {len(paragraphs)} paragraphs...")
    embeddings = model.encode(paragraphs, convert_to_tensor=True)
    return embeddings
