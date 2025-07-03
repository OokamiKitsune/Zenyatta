from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader, UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# Load all docs in the directory
loader = DirectoryLoader(
    "../docs/",
    glob="**/*",
    loader_cls=UnstructuredFileLoader,  # This will work for .txt files
)

# Also load PDFs
pdf_loader = DirectoryLoader(
    "../docs/",
    glob="**/*.pdf",
    loader_cls=UnstructuredPDFLoader
)

# Combine docs
docs = loader.load() + pdf_loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

print(f"Loaded {len(chunks)} chunks.")

# Embed and persist
embedding = OllamaEmbeddings(model="deepseek-r1")

db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="./chroma_db"
)

db.persist()
print("Vector DB persisted to ./chroma_db")