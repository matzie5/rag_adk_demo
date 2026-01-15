from google.adk.agents import Agent
from google.cloud import bigquery
from google.adk.tools import FunctionTool, ToolContext
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_ID_SMALL = "gemini-2.5-flash"
SALES_BULLETIN_TABLE = os.getenv("SALES_BULLETIN_TABLE")


def get_current_sales_bulletin() -> str:
    """
    Retrieves the latest weekly sales bulletin including strategy,
    focus products, and key selling points.
    """

    client = bigquery.Client()

    query = f"SELECT * FROM `{SALES_BULLETIN_TABLE}`"

    try:
        query_job = client.query(query)
        results = [dict(row) for row in query_job]

        if not results:
            return "No active bulletin found for this week."

        # Return the single row as a string representation of the dictionary
        return str(results[0])

    except Exception as e:
        return f"Database Error: {str(e)}"


get_sales_bulletin_tool = FunctionTool(
    func=get_current_sales_bulletin,
)


sales_bulletin_agent = Agent(
    name="sales_bulletin_agent",
    model=MODEL_ID_SMALL,
    instruction="""
        You are an internal data fetcher.
        1. Ignore the company name from the user query.
        2. Call the `get_current_sales_bulletin` tool to retrieve this week's sales strategy.
        3. Output the bulletin details clearly.

        ### RULES ###
        1. You MUST call the `get_current_sales_bulletin` tool ONLY ONCE.

    """,
    tools=[get_sales_bulletin_tool],
)
