# from google import genai
# import config

# genai.configure(api_key=config.GEMINI_API_KEY)

# genai_client = genai.Client(api_key=config.GEMINI_API_KEY)

# def embed_texts(texts: list[str]) -> list[list[float]]:
#     response = genai_client.models.embed_content(
#         model="gemini-embedding-001",
#         contents=texts
#     )
#     return response.embeddings

from sentence_transformers import SentenceTransformer

def embed_texts(texts: list[str]) -> list[list[float]]:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    return embeddings

