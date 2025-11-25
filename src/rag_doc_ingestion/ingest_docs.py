import logging

import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from src.rag_doc_ingestion.config.doc_ingestion_settings import DocIngestionSettings


#set up logging info
logging.basicConfig(  #logging is basically print statement ka upgrade version
    level=logging.INFO,  #tells kitni imp chizein dikhani h
    format='%(asctime)s - %(levelname)s - %(message)s' #design of your log message-->time, level(info/error/critical) and actual message
)

#creating a logger for this particular file
logger = logging.getLogger(__name__)

#load settings from environment variable
settings = DocIngestionSettings()  #storing the pydantic basesettings into this variable

#download and load embedding model
logger.info("Loading Hugging Face Embedding model...")  #time, info, and this message
embed_model = HuggingFaceEmbedding()


def build_vector_store_from_documents():
    logger.info("Starting process of vector store ingestion...")
    try:
        #configuring the directory
        docs_dir_path = settings.DOCUMENTS_DIR
        vector_store_path = settings.VECTOR_STORE_DIR
        collection_name = settings.COLLECTION_NAME
        logger.info(f"Loading documents from directory: {docs_dir_path}")
        loader = SimpleDirectoryReader(docs_dir_path)  #reading our dir path
        documents = loader.load_data()  #loading it

        #breaking the doc into chunks
        logger.info(f"{len(documents)} has been loaded and now a parser will be created")
        parser = SimpleNodeParser.from_defaults(chunk_size=1024, chunk_overlap=50)
        logger.info("Parsing documents...")
        nodes = parser.get_nodes_from_documents(documents)
        logger.info(f"{len(nodes)} has been parsed")

        #initializing vectordb-->chromadb
        logger.info(f"Initializing ChromaDB VectorStore at {vector_store_path}")
        db = chromadb.PersistentClient(path=vector_store_path)

        #create or retrieve the vector collection
        logger.info("Creating a chroma collection to store our parsed documents")
        chroma_collection = db.get_or_create_collection(name=collection_name)
        logger.info(f"Chroma collection created with name: {collection_name}! Creating chroma vector store...")
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

        #create storage context
        logger.info("Building storage context to wrap vector store")
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        logger.info("Building VectorStoreIndex")
        index = VectorStoreIndex(
            nodes=nodes,
            storage_context=storage_context,
            vector_store=vector_store,
            embed_model=embed_model,
        )
        logger.info("Vector Store built successfully")
        return 0
    except Exception as e:
        logger.error(f"Error during vector store build: {e}")
        return 1


if __name__ == "__main__":
    build_vector_store_from_documents()



