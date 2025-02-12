from agno.agent import Agent
from dotenv import load_dotenv  # Import the python-dotenv package
load_dotenv()  # Loads environment variables from .env

agent = Agent(markdown=True, monitoring=True)
agent.print_response("Share a 2 sentence horror story")
