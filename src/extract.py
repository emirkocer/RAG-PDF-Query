import fitz
import nltk
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Parameters:
    - pdf_path (str): Path to the PDF file.

    Returns:
    - str: Extracted text from the PDF.
    """
    try:
        with fitz.open(pdf_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None
    
def chunk_text_into_sentences(text):
    """
    Splits the input text into sentences using nltk.

    Parameters:
    - text (str): Input text.

    Returns:
    - List[str]: List of sentences.
    """
    try:
        sentences = nltk.sent_tokenize(text)
        return [sentence.strip() for sentence in sentences]
    except Exception as e:
        print(f"Error splitting text into sentences: {e}")
        return []
    
def chunk_text_into_paragraphs(text):
    """
    Splits text into paragraphs using double newlines as separators.

    Parameters:
    - text (str): Input text from the document.

    Returns:
    - List[str]: List of paragraphs.
    """
    try:
        # Split on double newlines or equivalent patterns
        paragraphs = re.split(r"\n\s*\n", text)
        return [para.strip() for para in paragraphs if para.strip()]
    except Exception as e:
        print(f"Error splitting text into paragraphs: {e}")
        return []
    
# Splits the text into pages based on the "Seite X" pattern.
def chunk_text_into_pages(text):
    """
    Splits the text into pages based on the "Seite X" pattern.

    Parameters:
    - text (str): Input text.

    Returns:
    - List[str]: List of pages.
    """
    try:
        # Split text at "Seite X" markers
        pages = re.split(r"(?m)^Seite\s+", text)
        return [page.strip() for page in pages if page.strip()]
    except Exception as e:
        print(f"Error splitting text into pages: {e}")
        return []