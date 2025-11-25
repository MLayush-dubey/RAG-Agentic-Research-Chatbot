from dotenv import load_dotenv
from pydantic_settings import BaseSettings

#load env variables from .env
load_dotenv()


class DocIngestionSettings(BaseSettings):
    """Settings for documentation ingestion"""
    DOCUMENTS_DIR: str  #this is from the env
    VECTOR_STORE_DIR: str
    COLLECTION_NAME: str

    class Config:  #this tells that look for a file called .env
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow" #"allow extra variables beyond what I defined" (so other settings in your .env won't cause errors).