from dotenv import load_dotenv
load_dotenv()
from tavily import TavilyClient
from langgraph.checkpoint.memory import InMemorySaver
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
tavily_client = TavilyClient()
@tool
def web_search(query: str) -> dict[str, any]:
    """Search the web for Infomration"""
    return tavily_client.search(query)

system_prompt = """
You are an expert personal chef assistant. Your primary objective is to create practical, delicious recipes based on whatever leftover or on-hand ingredients the user provides.

Guidelines:
1. Tool Usage: Utilize your web search tool to retrieve accurate recipe ideas, ingredient pairings, and cooking techniques when appropriate.
2. Pantry Optimization: Prioritize recipes that maximize the user's available ingredients while keeping extra required items to a minimum.
3. Recipe Structure: Present each recommended dish with:
   - Recipe Title & Estimated Prep/Cook Time
   - Required Ingredients (clearly marking which ones the user has vs. common pantry staples they may need)
   - Step-by-Step Cooking
   Instructions
4. Tone & Collaboration: Maintain an encouraging, culinary-focused tone and invite follow-up questions for substitutions or technique tips.
"""

agent = create_agent(
    model = "openai:gpt-5-nano",
    tools = [web_search],
    system_prompt=system_prompt,
    checkpointer=InMemorySaver()
)

config = {"configurable":{"thread_id": "1"}}

response = agent.invoke(
    {'messages':[HumanMessage(content="I have chicken and Rice at Home what I can make?")]},
    config=config
)

print(response['messages'][-1].content)