from multi_tool_agent.agent import root_agent

def handle_request(user_input):
    response = root_agent.run(input=user_input)
    return response
