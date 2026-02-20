# Simple RAG App with LangChain & OpenAI

A lightweight **RAG (Retrieval-Augmented Generation)** application that allows you to chat with your local text files using AI. 

## 🚀 Features
- **Document Loading**: Automatically reads and processes all `.txt` files in the directory.
- **Vector Search**: Uses **ChromaDB** for efficient local vector storage.
- **AI Chat**: Powered by **OpenAI (GPT-3.5/4)** to provide accurate answers based on your notes.
- **Persistent Loop**: Interactive command-line interface for continuous Q&A.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/mio_primo_rag.git](https://github.com/YOUR_USERNAME/mio_primo_rag.git)
   cd mio_primo_rag
   Set up a Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash
pip install python-dotenv langchain-openai langchain-community chromadb tiktoken
Environment Variables:
Create a .env file in the root folder and add your OpenAI API Key:

Plaintext
OPENAI_API_KEY=your_actual_key_here
📖 Usage
Place your notes in .txt files within the project folder.

Run the application:

Bash
python prova_rag_app.py
Ask questions about your documents in the terminal!

⚠️ Security Note
The .env file and venv/ folder are included in .gitignore to prevent leaking sensitive API keys and heavy environment files.
