import os
import nest_asyncio  # noqa: E402
nest_asyncio.apply()

from typing import Iterator
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# bring in our QDRANT_URL_LOCALHOST
from dotenv import load_dotenv
load_dotenv()


qdrant_url = os.getenv("QDRANT_URL_LOCALHOST")
llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")
chunk_size = 500
chunk_overlap = 50


import pickle
# Define a function to load parsed data if available, or parse if not
def load_or_parse_data():
    data_file = "./data/parsed_data.pkl"
    
    if os.path.exists(data_file):
        # Load the parsed data from the file
        with open(data_file, "rb") as f:
            parsed_data = pickle.load(f)
    else:
        # Perform the parsing step and store the result in llama_parse_documents
        parser = LlamaParse(api_key=llamaparse_api_key, result_type="markdown")
        #llama_parse_documents = parser.load_data("./data/DeepSeek_R1.pdf")
        file_extractor = {".pdf": parser}
        llama_parse_documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()
        

        # Save the parsed data to a file
        with open(data_file, "wb") as f:
            pickle.dump(llama_parse_documents, f)
        
        # Set the parsed data to the variable
        parsed_data = llama_parse_documents
    
    return parsed_data
            

# Create vector database
def create_vector_database():
    
     # Call the function to either load or parse the data
    llama_parse_documents = load_or_parse_data()
    #print(llama_parse_documents)
    print(llama_parse_documents[0].text[:100])
    
    with open('data/output_llamaparse.md', 'a') as f:  # Open the file in append mode ('a')
        for doc in llama_parse_documents:
            f.write(doc.text + '\n')
    
    loader = DirectoryLoader('data/', glob="**/*.md", show_progress=True)
    
    # Split loaded documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    documents = loader.load()
    splits = text_splitter.split_documents(documents)
    
    
    # Initialize Embeddings
    embeddings = FastEmbedEmbeddings()
    
    # Create and persist a Chroma vector database from the chunked documents
    vectorstore = QdrantVectorStore.from_documents(
        documents=splits,
        embedding=embeddings,
        url=qdrant_url,
        collection_name="rag-llamaparse",
    )
    
    print('Vector DB created successfully !')


if __name__ == "__main__":
    create_vector_database()