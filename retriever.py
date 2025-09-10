from embedder import embed_texts
from vector_store import query_vector

def retrieve(query, top_k=5):
    query_embedding = embed_texts([query])[0]
    results = query_vector(query_embedding, top_k=top_k)
    return results
