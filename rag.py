import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def setup_rag():

    documents = []

    for file in os.listdir("data"):
        if file.endswith(".txt"):
            loader = TextLoader(f"data/{file}")
            documents.extend(loader.load())

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        docs,
        embeddings
    )

    return vectorstore


def retrieve_context(vectorstore, query):
    results = vectorstore.similarity_search(query, k=4)
    return "\n".join([doc.page_content for doc in results])