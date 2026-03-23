import warnings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core._api.deprecation import LangChainDeprecationWarning
# warnings.filterwarnings("ignore",category=LangChainDeprecationWarning)


# file=input("Enter the filename->")
# filename=file+".pdf"
def ingest_pdf(filepath):
    loader=PyMuPDFLoader(filepath)
    documents=loader.load()

    
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks=text_splitter.split_documents(documents)


    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    vectordb=Chroma(persist_directory="BOT_DB",
                              embedding_function=embeddings)

    vectordb.add_documents(chunks)
    vectordb.persist()

