import re

MODEL_DEFAULT = "all-MiniLM-L6-v2"
MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" # for German text

DATABASE_NAME = "tax_law" # ChromaDB collection name
SIMILARITY_THRESHOLD = 0.5

def preprocess_text(text):
    """
    Preprocesses text to handle abbreviations, newlines, and spaces.

    Parameters:
    - text (str): Input text.

    Returns:
    - str: Preprocessed text.
    """
    # Replace common abbreviations
    abbreviations = {"Nr.": "NR_ABBREV", "Abs.": "ABS_ABBREV", "Rz.": "RZ_ABBREV", "EStG": "ESTG"}
    for abbr, placeholder in abbreviations.items():
        text = text.replace(abbr, placeholder)
    
    # Normalize spaces and merge lines
    text = re.sub(r"\s+", " ", text)
    return text

