import uuid
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import config


def load_and_chunk(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs)

    # Attach UUID4
    for chunk in chunks:
        chunk.metadata["id"] = str(uuid.uuid4())
        chunk.metadata["source"] = file_path
        chunk.metadata["page"] = chunk.metadata.get("page", None)
        chunk.metadata["title"] = file_path.split("/")[-1]  # fallback as filename

    return chunks


