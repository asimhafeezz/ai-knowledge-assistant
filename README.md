# 🧠 AI Knowledge Assistant

The **AI Knowledge Assistant** is a powerful tool that enables users to interact with their documents through natural language. Powered by LLMs and retrieval-augmented generation (RAG), it lets you upload documents and ask questions — receiving context-aware, intelligent answers instantly.

---

### [DEMO](https://drive.google.com/file/d/15pVdIqxVfS1C-Um4C5XD3LB5WWw9o-1s/view?usp=sharing)

---

## Key Features

- 🔍 **Contextual Question Answering**  
  Ask detailed questions and receive accurate answers grounded in your uploaded files.

- 📄 **Multi-format Support**  
  Upload documents in `.pdf`, `.txt`, or `.md` formats.

- ⚡ **Fast & Lightweight**  
  Built entirely in Streamlit — no backend or database setup required.

- 🧠 **RAG Pipeline with LlamaIndex**  
  Combines ChromaDB vector storage and GPT-4 to deliver reliable and explainable responses.

- 💬 **Clean Chat Interface**  
  Intuitive left/right message styling, real-time response, and persistent chat history.

---

## Tech Stack
	•	Streamlit — UI & deployment
	•	LlamaIndex — document parsing, RAG pipeline
	•	ChromaDB — local vector store
	•	OpenAI GPT-4 — LLM for reasoning
	•	Python 3.10+

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-knowledge-base-assistant.git
cd ai-knowledge-base-assistant
```

### 2. Set up a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a .env file in the project root:
```bash
OPENAI_API_KEY=your-openai-api-key
```

### 5. Run the application

```bash
streamlit run main.py
```

Built by Asim!
