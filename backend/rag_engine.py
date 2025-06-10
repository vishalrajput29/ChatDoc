from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_groq import ChatGroq

from backend.config import GROQ_API_KEY, EMBEDDING_MODEL

embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def create_vectorstore(documents):
    all_chunks = []
    for doc in documents:
        full_doc = Document(page_content=doc["content"], metadata={"source": doc["filename"]})
        chunks = splitter.split_documents([full_doc])
        all_chunks.extend(chunks)
    vectorstore = FAISS.from_documents(all_chunks, embedding_model)
    return vectorstore

def query_vectorstore(vectorstore, query):
    docs = vectorstore.similarity_search(query, k=5)
    
    results = []
    for doc in docs:
        result = {
            "Document ID": doc.metadata.get("source", "Unknown"),
            "Extracted Answer": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content,
            "Citation": doc.metadata.get("location", "N/A")  # optional metadata for page/para if added
        }
        results.append(result)

    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer in detail with source references."
    answer = llm.invoke(prompt)
    
    return answer, results

