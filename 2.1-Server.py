from dotenv import load_dotenv
load_dotenv()
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from langchain_core.tools import tool
from requests import get
from typing import Dict, Any

mcp = FastMCP("mcp_server")
tavily_client = TavilyClient()

@mcp.tool()
def search_web(query:str) -> Dict[str, Any]:
    """search the web for information"""
    return tavily_client.search(query)

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SearchServer")


@mcp.resource("config://search-guidelines")
def search_guidelines() -> str:
    """Guidelines and rules for using web search effectively."""
    return """
    Search Rules:
    1. Only use Tavily search when user asks about real-time, current events or facts.
    2. Format queries concisely without conversational words.
    3. Maximum 3 queries per user request.
    4. Always summarize findings with source citations.
    """
