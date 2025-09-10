# import cohere
# import config

# co = cohere.Client(config.COHERE_API_KEY)

# def rerank(query, results):
#     texts = [match['metadata']['text'] for match in results['matches']]
#     metadatas = [match['metadata'] for match in results['matches']]

#     rerank_results = co.rerank(
#         model="rerank-english-v2.0",
#         query=query,
#         documents=texts,
#         top_n=3
#     )
#     reranked_chunks = []
#     for item in rerank_results.results:
#         reranked_chunks.append({
#             "text": texts[item.index],
#             "metadata": metadatas[item.index]
#         })
#     return [texts[item.index] for item in rerank_results.results]


# ------------------------------------------------------------------------------------------------------------------
from sentence_transformers import CrossEncoder

# Load free cross-encoder model
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, results, top_n=3):
    texts = [match['metadata']['text'] for match in results['matches']]
    scores = model.predict([(query, t) for t in texts])
    
    # Sort by score
    ranked = sorted(zip(texts, results['matches'], scores), key=lambda x: x[2], reverse=True)
    
    reranked_chunks = []
    for i, (text, meta, score) in enumerate(ranked[:top_n]):
        reranked_chunks.append({
            "text": text,
            "metadata": meta['metadata'],
            "score": float(score)
        })
    return reranked_chunks
