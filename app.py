import streamlit as st
from backend.loader import load_documents
from backend.rag_engine import create_vectorstore, query_vectorstore
from backend.theme_identifier import identify_themes
import os
st.set_page_config(page_title="RAG Theme Chatbot", layout="wide")
st.title("🧵 Document Research & Theme Chatbot")

uploaded_files = st.file_uploader("Upload Documents (PDF, PNG, JPG)", accept_multiple_files=True)

if "docs" not in st.session_state:
    st.session_state.docs = []
    st.session_state.vectorstore = None

if uploaded_files:
    with st.spinner("Processing documents..."):
        temp_folder = "temp_uploads"
        os.makedirs(temp_folder, exist_ok=True)
        for uploaded in uploaded_files:
            path = os.path.join(temp_folder, uploaded.name)
            with open(path, "wb") as f:
                f.write(uploaded.read())
        st.session_state.docs = load_documents(temp_folder)
        st.session_state.vectorstore = create_vectorstore(st.session_state.docs)
        st.success("Documents processed and indexed.")

query = st.text_input("Ask a question about the documents")
if st.button("Submit") and query:
    if not st.session_state.vectorstore:
        st.warning("Please upload documents first.")
    else:
        with st.spinner("Querying documents..."):
            answer, sources = query_vectorstore(st.session_state.vectorstore, query)
            st.subheader("Answer")
            st.write(answer)
            st.subheader("Sources")
            st.write(", ".join(set(sources)))
            theme_summary = identify_themes([answer.content if hasattr(answer, 'content') else str(answer)])

            st.subheader("Identified Themes")
            st.markdown(theme_summary)