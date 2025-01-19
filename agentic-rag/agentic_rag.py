from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
from phi.model.ollama import Ollama
from phi.embedder.ollama import OllamaEmbedder
from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.qdrant import Qdrant
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.knowledge.website import WebsiteKnowledgeBase
import os

from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_URL_LOCAL = os.getenv('QDRANT_URL_LOCALHOST')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# create vectordb
vector_db = Qdrant(
    collection="phidata-qdrant-ytpy",
    #url=QDRANT_URL,
    url=QDRANT_URL_LOCAL,
    #api_key=QDRANT_API_KEY,
    embedder = OllamaEmbedder(),
)

URL = "https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"

knowledge_base = PDFUrlKnowledgeBase(
    urls = [URL],
    vector_db = vector_db,
)

# Load the knowledge base: Comment after first run as the knowledge base is already loaded
#knowledge_base.load(upsert=True)

agent_ollama = Agent(
    model=Ollama(id="llama3.1:8b"),
    #model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Set as False because Agents default to `search_knowledge=True`
    search_knowledge=True,
    show_tool_calls=True,
    markdown=True,
    
    #storage=SqlAgentStorage(table_name="phidata", db_file="agents_rag.db"),
    #add_history_to_messages=True,
)

#agent_ollama.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)


agent_ollama.print_response(
    "Hi, i want to make a 3 course meal. Can you recommend some recipes. "
    "I'd like to start with a soup, then im thinking a thai curry for the main course and finish with a dessert",
    stream=True,
)