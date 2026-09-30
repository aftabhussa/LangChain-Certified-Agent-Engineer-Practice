from typing import Dict, Any
from mcp.server.fastmcp import FastMCP

client = FastMCP()
@mcp.tools("Search_Web")

def search_web(query: str) -> Dict[str, Any]:
    