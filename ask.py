from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from init import init_nlp_resources
import re

# We will keep these as module-level variables so they initialize only once
qa = None

def initialize_retrieval_pipeline():
    global qa

    # Initialize NLTK or other NLP resources
    init_nlp_resources()

    # Load documents from the directory
    embedding = OllamaEmbeddings(model="deepseek-r1")
    db = Chroma(
        persist_directory="./util/chroma_db",
        embedding_function=embedding,
    )


    retriever = db.as_retriever(search_kwargs={"k": 8})

    llm = Ollama(model="deepseek-r1")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

def answer_question(query):
    """
    Call this function from your Gradio UI.
    Returns the answer string with sources.
    """

    def clean_response(text):
        """
        Remove <think>...</think> blocks or any other reasoning markup.
        """


    global qa
    if qa is None:
        raise RuntimeError("Retrieval pipeline is not initialized. Call initialize_retrieval_pipeline() first.")

    result = qa({"query": query})
    answer = result["result"]
    sources = "\n".join([doc.metadata["source"] for doc in result["source_documents"]])
    return f"{answer}\n\nSources:\n{sources}"