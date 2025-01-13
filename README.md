# **RAG-PDF-Query**

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline to answer questions about a collection of PDF documents. The pipeline combines text extraction, vectorization, and a semantic search using **ChromaDB** to retrieve relevant information, followed by a GPT-4-powered answer generation step.

---

## **1. Features**

- Extracts text from a collection of PDF files.
- Processes and chunks the text into paragraphs for efficient vectorization.
- Stores the vectorized data into a vector database using **ChromaDB**.
- Retrieves relevant context for a given query using semantic similarity.
- Generates accurate and contextually grounded answers using **GPT-4** for three test questions.
- Interactive CLI to allow users to ask additional questions beyond predefined ones.

---

## **2. Requirements**

#### **Python Environment**
Ensure you have Python 3.8 or later installed.

#### **Install Dependencies**
Install the required libraries via `pip`:
```bash
pip install -r requirements.txt
```
#### **Additional Setup**
Add your OpenAI API key to a .env file in the root directory. 

```bash
OPENAI_API_KEY=your_openai_api_key
```

---

## **3. Usage**

#### **Prepare Your PDF Files**
- Place all relevant PDF files in the `../data/` folder.

#### **Run the Script**
Run the script using:
```bash
python3 main.py
```

#### **Enter Query**

The script will answer predefined questions given in the test_questions module and display results. Then, it will enter the interactive mode and prompt you to ask additional questions.

Type your question, an answer will be provided based on the document contex using the RAG-pipeline.

You can exit the interactive mode by typing
```bash
exit
```


---

## **4. Configuration**


The predefined questions are located in `test_questions.py`. You can edit this file to add or modify questions.

The embedding model is defined in `utils.py`.

**IMPORTANT NOTE:** make sure that the selected embedding model supports the language of the data files and questions !

---

## **5. Folder Structure**

```plaintext
.
├── data/                 # Folder for PDF files
├── src/                  # Source code folder
│   ├── main.py           # Control file - entry point of the project
│   ├── extract.py        # PDF text extraction and chunking functions
│   ├── vectorize.py      # Vectorization of paragraphs
│   ├── database.py       # ChromaDB collection and storage functions
│   ├── query.py          # Context retrieval functions
│   ├── utils.py          # Utilities and global settings
│   ├── prompts.py        # System and user prompt templates
│   ├── test_questions.py # Predefined questions
├── .env                  # Environment variables (e.g., OpenAI API key)
├── requirements.txt      # Python dependencies

```