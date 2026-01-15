from google.adk.agents import Agent
from google.adk.tools import google_search

MODEL_ID_SMALL = "gemini-2.5-flash"

news_agent = Agent(
    name="news_agent",
    model=MODEL_ID_SMALL,
    instruction="""
    You are an agent specialized in retrieving recent news about a company provided by the user.
    Return 5 recent significant news about the company utilizing 'google_search' tool.
    """,
    tools=[google_search],
)
