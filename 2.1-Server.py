import os
from typing import Any, Dict
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient

# 1. Environment variables (.env se TAVILY_API_KEY) load karein
load_dotenv()

# 2. FastMCP Server aur Tavily Client initialize karein
mcp = FastMCP("mcp_server")
tavily_client = TavilyClient()


# 3. Web Search Tool
@mcp.tool()
def search_web(query: str) -> Dict[str, Any]:
    """search the web for information"""
    return tavily_client.search(query)


# 4. Search Guidelines Resource
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


# 5. Local Subprocess Run Entrypoint (Lazmi hai stdio transport ke liye)
if __name__ == "__main__":
    mcp.run(transport="stdio")