import os
from dotenv import load_dotenv
from google.adk.tools import VertexAiSearchTool

load_dotenv()

PRODUCT_DATASTORE_ID = os.getenv("PRODUCT_DATASTORE_ID")
SALES_KNOWLEDGE_DATASTORE_ID = os.getenv("SALES_KNOWLEDGE_DATASTORE_ID")


def get_product_tool():
    return VertexAiSearchTool(
        data_store_id=PRODUCT_DATASTORE_ID,
    )


def get_sales_knowledge_tool():
    return VertexAiSearchTool(
        data_store_id=SALES_KNOWLEDGE_DATASTORE_ID,
    )
