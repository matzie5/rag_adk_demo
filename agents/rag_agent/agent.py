from google.adk.agents import SequentialAgent
from .sub_agents.news_agent import news_agent
from .sub_agents.rag_agent import rag_agent
from .sub_agents.sales_bulletin_agent import sales_bulletin_agent

root_agent = SequentialAgent(
    name="NewsRagPipeline",
    description="A pipeline that ingests data and generates a report.",
    sub_agents=[news_agent, sales_bulletin_agent, rag_agent],
)

print(f"My Root Agent '{root_agent.name}'")
