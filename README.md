# Financial P&L BOT Using ML

Overview
This project implements a Financial Statement Question Answering Chatbot using a Retrieval-Augmented Generation (RAG) architecture.
The system allows users to upload financial statement PDFs and ask natural language questions such as:

What is the net profit?
What is the gross profit?
What are the operating expenses?
What is the profit before tax?
The chatbot retrieves relevant financial information from the uploaded document and returns a precise answer based on the report content.

Architecture
User Uploads Financial PDF
↓
PDF Text Extraction (PyMuPDF)
↓
Text Chunking
↓
Embedding Generation (SentenceTransformers)
↓
Vector Storage (Pinecone)
↓
User Question
↓
Query Embedding
↓
Vector Similarity Search
↓
Relevant Financial Context Retrieved
↓
QA Model Extracts Final Answer

This approach improves accuracy by retrieving relevant document content before answering the question.

Tech Stack
Python
Primary programming language used to implement the entire pipeline.

Google Colab
Used for development and running the notebook environment.

PyMuPDF (fitz)
Used for extracting text content from uploaded financial statement PDFs.

SentenceTransformers
Used to convert document text chunks into vector embeddings that capture semantic meaning.

Model used:

all-MiniLM-L6-v2
Pinecone
Vector database used to store embeddings and perform similarity search to retrieve relevant document chunks.

Vector settings: - Dimension: 384 - Metric: Cosine similarity

HuggingFace Transformers
Used to run the Question Answering model that extracts the exact answer from retrieved context.

Model used:

deepset/roberta-base-squad2
Gradio
Used to build a simple web interface where users can: - Upload financial statements - Process the document - Ask financial questions - Receive answers

Project Workflow
1. Upload Financial Statement
User uploads a financial PDF using the Gradio interface.

2. Text Extraction
PyMuPDF extracts text from all pages of the document.

3. Text Chunking
The extracted text is split into smaller chunks to improve embedding quality and retrieval accuracy.

4. Embedding Generation
Each chunk is converted into a vector embedding using SentenceTransformers.

5. Vector Storage
Embeddings are stored in Pinecone along with metadata containing the original text.

6. Question Processing
When a user asks a question: - The question is converted into an embedding - Pinecone performs similarity search - The most relevant chunks are retrieved

7. Answer Extraction
A HuggingFace QA model extracts the most relevant answer from the retrieved context.

Features
Upload financial statement PDFs
Ask natural language financial questions
Accurate document-based answers
Vector search powered retrieval
Interactive Gradio interface
Scalable RAG architecture
Example Questions
Users can ask questions like:

What is the net profit?
What is the gross profit?
What is the profit before tax?
What are the operating expenses?
How much tax expense is reported?
Installation
Install required dependencies:

pip install pinecone sentence-transformers transformers pymupdf gradio
How to Run
Open the notebook in Google Colab
Run all cells
Upload a financial statement PDF
Click Process Document
Ask financial questions in the interface
Repository Structure
financial-qa-chatbot
│
├── financial_qa_chatbot.ipynb
├── sample_financial_statement.pdf
├── README.md
├── requirements.txt
Future Improvements
Possible improvements include:

Table-aware financial data extraction
Improved chunking strategy for financial tables
Support for multiple document uploads
Integration with larger language models
Deployment as a web application
Author
Jithendra

AI & Machine Learning Engineer