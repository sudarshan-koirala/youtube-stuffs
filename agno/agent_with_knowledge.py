from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

from dotenv import load_dotenv  # Import the python-dotenv package
load_dotenv()  # Loads environment variables from .env

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="You are a Thai cuisine expert!",
    instructions=[
        "Search your knowledge base for Thai recipes.",
        "If the question is better suited for the web, search the web to fill in gaps.",
        "Prefer the information in your knowledge base over the web results."
    ],
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipes",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Comment out after the knowledge base is loaded
#if agent.knowledge is not None:
#    agent.knowledge.load()

#agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)
agent.print_response("What is the history of Thai curry?", stream=True)
