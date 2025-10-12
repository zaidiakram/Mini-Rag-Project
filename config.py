import os
import streamlit as st

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY"," ")
PINECONE_INDEX = "rag-768"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", " ")
COHERE_API_KEY = os.getenv("COHERE_API_KEY", " ")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
