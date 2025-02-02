import os
# import nest_asyncio  # noqa: E402
# nest_asyncio.apply()

from typing import Iterator
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument
from docling.document_converter import DocumentConverter

# bring in our QDRANT_URL_LOCALHOST
from dotenv import load_dotenv
load_dotenv()


qdrant_url = os.getenv("QDRANT_URL_LOCALHOST")
chunk_size = 300
chunk_overlap = 30



class DoclingPDFLoader(BaseLoader):
    def __init__(self, file_path: str | list[str]) -> None:
        self._file_paths = file_path if isinstance(file_path, list) else [file_path]
        self._converter = DocumentConverter()

    def lazy_load(self) -> Iterator[LCDocument]:
        for source in self._file_paths:
            dl_doc = self._converter.convert(source).document
            text = dl_doc.export_to_markdown()
            yield LCDocument(page_content=text)
            


# Create vector database
def create_vector_database():
        
    loader = DoclingPDFLoader(file_path="./data/deepseek_R1.pdf")
    # Split loaded documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docling_documents = loader.load()
    
    with open('data/output_docling.md', 'a') as f:  # Open the file in append mode ('a')
        for doc in docling_documents:
            f.write(doc.page_content + '\n')
        
        
    splits = text_splitter.split_documents(docling_documents)
    
    
    # Initialize Embeddings
    embeddings = FastEmbedEmbeddings()
    
    # Create and persist a Qdrant vector database from the chunked documents
    vectorstore = QdrantVectorStore.from_documents(
        documents=splits,
        embedding=embeddings,
        url=qdrant_url,
        collection_name="rag",
    )
    
    print('Vector DB created successfully !')


if __name__ == "__main__":
    create_vector_database()