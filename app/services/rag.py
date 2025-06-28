import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import pandas as pd
from typing import List, Tuple
import yaml
from app.services.data_access import get_accessible_documents

# Load config and initialize
with open("resources/data/config.yaml", "r") as f:
    config = yaml.safe_load(f)
os.environ["GROQ_API_KEY"] = config["groq_api_key"]
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatGroq(
    groq_api_key=config["groq_api_key"],
    model_name="llama-3.1-8b-instant"
)

# Access rules for document visibility based on user roles
def load_and_index_documents(doc_paths: List[str]) -> FAISS:
    texts, metadatas = [], []
    for doc_path in doc_paths:
        possible_paths = [
            f"resources/data/{doc_path}",
            f"resources/data/finance/{doc_path}",
            f"resources/data/marketing/{doc_path}",
            f"resources/data/engineering/{doc_path}",
            f"resources/data/general/{doc_path}",
            f"resources/data/hr/{doc_path}",
        ]
        full_path = next((p for p in possible_paths if os.path.exists(p)), None)
        if not full_path:
            print(f"Warning: {doc_path} not found in expected locations. Skipping.")
            continue
        print(f"Loading document: {full_path}")  # DEBUG
        if doc_path.endswith(".csv"):
            df = pd.read_csv(full_path)
            for _, row in df.iterrows():
                texts.append(row.to_string())
                metadatas.append({"source": doc_path})
        else:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
                texts.append(content)
                metadatas.append({"source": doc_path})
    if not texts:
        raise FileNotFoundError("No valid documents found to index.")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.create_documents(texts, metadatas=metadatas)
    print(f"Total chunks created: {len(chunks)}")  # DEBUG
    return FAISS.from_documents(chunks, embeddings)

# Get accessible documents based on user role
def process_query(query: str, role: str) -> Tuple[str, List[str]]:
    doc_paths = get_accessible_documents(role)
    print(f"Docs being indexed for this user/role: {doc_paths}") 
    vector_store = load_and_index_documents(doc_paths)
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs if doc.page_content.strip()])

    print("\n--- Retrieved Context ---\n", context) 

    if not context.strip():
        print("--- No context found for query. Returning fallback. ---")
        return (
            "Sorry, I couldn't find relevant information in your accessible documents for this query.",
            []
        )

    prompt = f"""
You are FinSolve's internal AI assistant. You must answer using only the context below, which is based on the user's role: {role}.
If the answer is not in the context, say "I don't know based on the available documents." Do NOT make up information.

User Query: {query}

Context:
{context}
"""
    print("\n--- Prompt sent to LLM ---\n", prompt) 

    try:
        response = llm.invoke(prompt)
        return response.content, [doc.metadata["source"] for doc in docs]
    except Exception as e:
        print("LLM error:", e)
        return (
            "Sorry, the AI service is temporarily unavailable. Please try again later.",
            []
        )