from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader, UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from config import Config


# Load all docs in the directory
print("Loading documents from ../docs/...")
loader = DirectoryLoader(
    "../docs/",
    glob="**/*",
    loader_cls=UnstructuredFileLoader,  # This will work for .txt files
)

# Also load PDFs
print("💾Loading PDF documents from ../docs/...")
pdf_loader = DirectoryLoader(
    "../docs/",
    glob="**/*.pdf",
    loader_cls=UnstructuredPDFLoader
)

# Combine docs
docs = loader.load() + pdf_loader.load()

# Split into chunks
print(f"💾Loaded {len(docs)} documents. Splitting into chunks...")
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

print(f"Loaded {len(chunks)} chunks.")

# Embed and persist
print("💾Generating embeddings and persisting to Chroma DB...")
embedding = OllamaEmbeddings(model=Config.EMBEDDING_MODEL)

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./chroma_db"
)

db.persist()
print(f"✅Vector DB generated and persisted to {Config.DATABASE_PATH}")