from loader import load_and_chunk
from embedder import embed_texts
from vector_store import upsert
from retriever import retrieve
from reranker import rerank
from llm import generate_response




def build_knowledge_base(file_path):
    chunks = load_and_chunk(file_path)
    embeddings = embed_texts([chunk.page_content for chunk in chunks])
    upsert(chunks, embeddings)
    print(f"Inserted {len(chunks)} chunks into Pinecone.")

def ask_question(query):
    results = retrieve(query, top_k=10)
    reranked_chunks = rerank(query, results)
    answer, cited_chunks = generate_response(query, reranked_chunks)
    return answer, cited_chunks

if __name__ == "__main__":
    # 1. Load data into Pinecone (only once)
    build_knowledge_base("Enhanced RAG.pdf")
    
  
    # 2. Ask question
    query = "What is the main topic of the document?"
    print("Q:", query)
    print("A:", ask_question(query))



