# import pinecone
from pinecone import Pinecone, ServerlessSpec
import config

# pinecone.init(api_key=config.PINECONE_API_KEY)
# if config.PINECONE_INDEX not in pinecone.list_indexes():
#     pinecone.create_index(config.PINECONE_INDEX, dimension=768)  # depends on embedding size

# index = pinecone.Index(config.PINECONE_INDEX)

# def upsert(chunks, embeddings):
#     # embeddings and chunks must align
#     vectors = []
#     for chunk, embedding in zip(chunks, embeddings):
#         vectors.append((chunk.metadata["id"], embedding, {"text": chunk.page_content}))
#     index.upsert(vectors)

# def query_vector(vector, top_k=5):
#     return index.query(vector=vector, top_k=top_k, include_metadata=True)
# --------------------------------------------------------------------------------------------------


# Initialize Pinecone client
pc = Pinecone(api_key=config.PINECONE_API_KEY)
print(pc.list_indexes())

# Create index if it doesn’t exist
if config.PINECONE_INDEX not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=config.PINECONE_INDEX,
        dimension=768,  
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Connect to index
index = pc.Index(config.PINECONE_INDEX)

def upsert(chunks, embeddings):
    vectors = []
    for chunk, embedding in zip(chunks, embeddings):
        vectors.append({
            "id": chunk.metadata["id"],
            "values": embedding,
            "metadata": {
                "text": chunk.page_content,
                "source": chunk.metadata.get("source"),
                "page": chunk.metadata.get("page"),
                "title": chunk.metadata.get("title"),
            }
        })
    index.upsert(vectors=vectors)

def query_vector(vector, top_k=5):
    return index.query(vector=vector, top_k=top_k, include_metadata=True)


# Clear old PDF helper

# def clear_old_pdf(pdf_title):
#     matches = index.query(filter={"metadata.title": pdf_title}, top_k=1000).get("matches", [])
#     ids = [m["id"] for m in matches]
#     if ids:
#         index.delete(ids=ids)
#         print(f"Deleted {len(ids)} vectors for PDF: {pdf_title}")
#     else:
#         print(f"No entries found for PDF: {pdf_title}")