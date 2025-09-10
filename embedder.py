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

import asyncio
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import config

# Ensure event loop exists in Streamlit's ScriptRunner thread
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())



embeddings_client = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=config.GEMINI_API_KEY
)

def embed_texts(texts: list[str]) -> list[list[float]]:
    return embeddings_client.embed_documents(texts)

