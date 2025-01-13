import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import utils


# Function to create a ChromaDB collection using the provided embedding function
def create_chromadb_database(collection_name, embedding_func=None):
    """
    Creates a ChromaDB collection if it doesn't already exist.

    Parameters:
    - collection_name (str): Name of the ChromaDB collection.

    Returns:
    - collection: The created or retrieved ChromaDB collection.
    """
    # Initialize ChromaDB client
    print("Initializing ChromaDB client...")
    client = chromadb.Client(Settings())

    # Create or get a collection
    if embedding_func:
        collection = client.create_collection(collection_name, embedding_function=embedding_func)
    else:
        collection = client.create_collection(collection_name)

    print(f"Collection '{collection_name}' is ready.")
    
    return collection

# Function to store vectorized paragraphs in a ChromaDB collection
def store_into_collection(paragraphs, embeddings, collection):
    """
    Stores vectorized paragraphs in a ChromaDB collection.

    Parameters:
    - paragraphs (List[str]): Original text paragraphs.
    - embeddings (List[ndarray]): Vectorized embeddings.
    - collection (Collection): ChromaDB collection.

    Returns:
    - None
    """
    # Add data to the collection
    for idx, (para, embedding) in enumerate(zip(paragraphs, embeddings)):
        collection.add(
            ids=[str(idx)],  # Provide a unique ID as a string for each document (must)
            documents=[para],
            metadatas={"id": idx},  # Add any additional metadata as needed
            embeddings=[embedding.cpu().numpy()]  # Convert tensor to NumPy array
        )

    print(f"Stored {len(paragraphs)} paragraphs in ChromaDB.")
