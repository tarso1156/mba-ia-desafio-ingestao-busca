import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class VectorStoreSingleton:
    _instance = None

    def __new__(self):
        if self._instance is None:
            embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small",
                openai_api_key=OPENAI_API_KEY
            )

            self._instance = PGVector(
                embeddings=embeddings,
                collection_name=PG_VECTOR_COLLECTION_NAME,
                connection=DATABASE_URL,
                use_jsonb=True,
            )

        return self._instance

vector_db  = VectorStoreSingleton()
