# servers/serp-mcp/server.py
from fastmcp import FastMCP, Context

import requests
from duckduckgo_search import DDGS
import traceback
from typing import List, Dict, Any

server = FastMCP("serp")



# @server.tool()
# def search(query: str) -> str:
#     """Search the web using DuckDuckGo and return short text results."""
#     url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
#     res = requests.get(url).json()
#     return res.get("AbstractText", "No results")

@server.tool()
async def search(query: str, ctx: Context, max_results: int = 5) -> str:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "No results"

        formatted = "\n".join(f"{i+1}. {r['title']} — {r['href']}" for i, r in enumerate(results))
        return formatted
    except Exception as e:
        await ctx.error(f"Failed: {str(e)}")
        traceback.print_exc()
        return f"Error: {str(e)}"
    

@server.tool()
def google_search(query: str, num_results: int = 5) -> List[Dict[str, Any]]:
    """Search the web using Google via Serper API
    
    Args:
        query: Search query string
        num_results: Number of results to return (default: 5)
    
    Returns:
        List of search results with title, snippet, and url
    """
    import os
    API_KEY = os.getenv("SERPER_API_KEY")
    
    if not API_KEY:
        return [{"error": "Serper API key not configured"}]
    
    try:
        url = "https://google.serper.dev/search"
        headers = {
            'X-API-KEY': API_KEY,
            'Content-Type': 'application/json'
        }
        data = {
            'q': query,
            'num': num_results
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        results_data = response.json()
        organic_results = results_data.get('organic', [])
        
        formatted_results = []
        for result in organic_results:
            formatted_results.append({
                "title": result.get('title', ''),
                "snippet": result.get('snippet', ''),
                "url": result.get('link', ''),
                "source": "Google (via Serper)"
            })
        
        return formatted_results
        
    except Exception as e:
        return [{"error": f"Google search failed: {str(e)}"}]


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server.run(transport="stdio")

