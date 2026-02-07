import os
import time

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vectorstore import vector_db

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

def ingest_pdf():
    print(f"Carregando {PDF_PATH}...")
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=False
    )

    splits = text_splitter.split_documents(docs)
    if not splits:
        raise SystemExit(0)
    
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
        )
        for d in splits
    ]

    ids = [f"doc-{i}" for i in range(len(enriched))]

    batch_size = 20
    for i in range(0, len(splits), batch_size):
        enriched_batch = splits[i : i + batch_size]
        ids_batch = ids[i : i + batch_size]

        vector_db.add_documents(documents=enriched_batch, ids=ids_batch)

        time.sleep(1)
        

    print(f"Concluiu com sucesso a ingestão do PDF (Indexou com sucesso {len(splits)} splits)")

if __name__ == "__main__":
    ingest_pdf()