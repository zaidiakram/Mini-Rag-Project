import google.generativeai as genai
import config

genai.configure(api_key=config.GEMINI_API_KEY)

def generate_response(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Answer the following question using the provided context.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text




def generate_response(query, reranked_chunks):
    # Build context with citations
    context = ""
    for i, chunk in enumerate(reranked_chunks, start=1):
        md = chunk["metadata"]
        citation = f"[{i}] Source: {md.get('source')}, Page: {md.get('page')}, Title: {md.get('title')}"
        context += f"{citation}\n{chunk['text']}\n\n"

    prompt = f"""
        Answer the following question using the provided context. 
        Always cite sources at the end of the answer in the format [number].

        Context: {context}

        Question: {query}
        Answer:
        """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text, reranked_chunks

