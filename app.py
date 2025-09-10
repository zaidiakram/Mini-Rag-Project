import streamlit as st
from config import GEMINI_API_KEY,PINECONE_API_KEY,COHERE_API_KEY
from main import build_knowledge_base, ask_question



st.set_page_config(page_title="RAG Demo", page_icon="🤖", layout="wide")

st.title("🔎 RAG Application with Citations (Pinecone + Gemini + Cohere)")

# --- File Uploader ---
st.sidebar.header("📂 Upload Document")
uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    file_path = f"uploaded_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.sidebar.button("Build Knowledge Base"):
        with st.spinner("Processing and uploading to Pinecone..."):
            build_knowledge_base(file_path)
        st.success("✅ Document processed and stored in Pinecone")

# --- Query Section ---
st.subheader("Ask a Question")
query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if not query.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Fetching answer..."):
            answer, chunks = ask_question(query)

        st.markdown("### 📝 Answer")
        st.write(answer)

        st.markdown("### 📚 Citations")
        for i, chunk in enumerate(chunks, start=1):
            md = chunk["metadata"]
            st.markdown(
                f"**[{i}]** Source: `{md.get('source')}` | Page: `{md.get('page')}` | Title: `{md.get('title')}`"
            )
