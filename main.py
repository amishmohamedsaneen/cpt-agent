from agent.agent_runner import run_agent

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    result = run_agent(user_input)
    print("Agent:", result)
