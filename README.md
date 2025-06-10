### **🧵 RAG Theme Chatbot**


A document-based AI chatbot that lets users upload and query large sets of documents (PDFs, images, text) and returns:

* Answered questions with proper citations
* A document-wise result table
* Automatically extracted theme summaries

Built with Streamlit, Groq LLM (LLaMA 3), FAISS vector store, and Hugging Face embeddings.

---

## 🚀 Features

* Upload and process 75+ documents (PDF, scanned images, etc.)
* OCR support for scanned files
* Natural language question-answering using LLM
* Accurate document citations with extracted content
* Auto-generated theme summaries across multiple documents
* Download results as CSV
* Deployed via Streamlit and open source tools

---

## 🧠 Tech Stack

| Component    | Tool / Library                |
| ------------ | ----------------------------- |
| LLM          | Groq + LLaMA 3                |
| Embeddings   | Hugging Face Transformers     |
| Vector Store | FAISS                         |
| OCR          | Tesseract + PIL               |
| Backend      | Python (modular architecture) |
| Frontend     | Streamlit                     |
| Deployment   | Streamlite cloud  |

---

## 📂 Folder Structure

```
chatbot_theme_identifier/
├── app.py
├── .env
├── requirements.txt
├── README.md
└── backend/
    ├── config.py
    ├── loader.py
    ├── rag_engine.py
    ├── theme_identifier.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/chatbot_theme_identifier.git
cd chatbot_theme_identifier
```

### 2. Create Virtual Environment

```
conda create -p ./env python=3.10 
```

### 3. Install Requirements

```
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free Groq API key at: [https://console.groq.com](https://console.groq.com)

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 🧪 Sample Use

* Upload 2–75+ documents (PDFs or images)
* Ask a question like:
  "What penalties are discussed in these reports?"
* View the answer, individual document breakdown, and synthesized theme summary
* Download CSV report

---

## 📥 Deployment Options

You can deploy on:

* Render
* Hugging Face Spaces
* Railway
* Replit

---

## 🙌 Credits

Built with ❤️ by Vishal Rajput for the Wasserstoff GenAI Internship Challenge.

---

## Authors

- [@vishalrajput](https://github.com/vishalrajput29)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. GroqAPI |





## Project Demo

https://drive.google.com/file/d/15vQwak3p4TmzlpRSbqml5bzc3E_DTqbQ/view?usp=sharing

