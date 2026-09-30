from typing import Dict, Any

from langchain import mcp
from tavily import TavilyClient
from mcp.server.fastmcp import FastMCP

tavily_client = TavilyClient()
mcp = FastMCP()
@mcp.tools

def search_web(query: str) -> Dict[str, Any]:
    """Search the web for Information"""
    return tavily_client.search(query) 
    
