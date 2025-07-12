from langchain.tools import tool
import requests
import math

@tool
def search_web(query: str) -> str:
    """Searches the web and returns results."""
    return f"Search results for: {query} (placeholder)"  # Replace with real search API

@tool
def calculate(expression: str) -> float:
    """Evaluates a mathematical expression."""
    return eval(expression)

search_tool = search_web
python_tool = calculate
