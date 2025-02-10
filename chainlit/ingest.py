import os
# import nest_asyncio  # noqa: E402
# nest_asyncio.apply()

from typing import Iterator
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument
from langchain_docling import DoclingLoader
from docling.chunking import HybridChunker
from langchain_docling.loader import ExportType

# bring in our QDRANT_URL_LOCALHOST
from dotenv import load_dotenv
load_dotenv()


qdrant_url = os.getenv("QDRANT_URL_LOCALHOST")
EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
EXPORT_TYPE = ExportType.DOC_CHUNKS
FILE_PATH = "./data/DeepSeek_R1.pdf"
            


# Create vector database
def create_vector_database():
    
    loader = DoclingLoader(
        file_path=FILE_PATH,
        export_type=EXPORT_TYPE,
        chunker=HybridChunker(tokenizer=EMBED_MODEL_ID),
    )

    docling_documents = loader.load()
    
    # Determining the splits
    
    if EXPORT_TYPE == ExportType.DOC_CHUNKS:
        splits = docling_documents
    elif EXPORT_TYPE == ExportType.MARKDOWN:
        splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header_1"),
                ("##", "Header_2"),
                ("###", "Header_3"),
            ],
        )
        splits = [split for doc in docling_documents for split in splitter.split_text(doc.page_content)]
    else:
        raise ValueError(f"Unexpected export type: {EXPORT_TYPE}")
    
    
    with open('data/output_docling.md', 'a') as f:  # Open the file in append mode ('a')
        for doc in docling_documents:
            f.write(doc.page_content + '\n')
    
    
    # Initialize Embeddings
    embedding = HuggingFaceEmbeddings(model_name=EMBED_MODEL_ID)
    
    # Create and persist a Qdrant vector database from the chunked documents
    vectorstore = QdrantVectorStore.from_documents(
        documents=splits,
        embedding=embedding,
        url=qdrant_url,
        collection_name="rag",
    )
    
    print('Vector DB created successfully !')


if __name__ == "__main__":
    create_vector_database()