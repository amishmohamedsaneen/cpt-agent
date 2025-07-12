from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from .tools import search_tool, python_tool

llm = ChatOpenAI(model="gpt-4o")

tools = [search_tool, python_tool]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
)

def run_agent(user_input):
    return agent.run(user_input)
