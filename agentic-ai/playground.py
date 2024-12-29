from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name = "Web Agent",
    description = "This is the agent for searching content from the web",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools  = [DuckDuckGo()],
    instructions = ["Always include the sources"],
    show_tool_calls = True,
    markdown = True,
    debug_mode=True
)

#web_search_agent.print_response("What is the capital of Nepal?", stream=True)

finance_agent = Agent(
    name="Finance Agent",
    description = "Your task is to find the finance information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    debug_mode = True
)
#finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)