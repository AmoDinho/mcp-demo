# Agent

This is a simple agent that uses the OpenAI Agents Python library to interact with an MCP server. You can ask the agent to calculate the sum of two numbers, or to tell you a joke.

## Installation

1. Prerequisites:
   - Install required packages: pip install openai-agents openai
   - Set up environment variables:
     - OPENAI_API_KEY: Your OpenAI API key
     - AGENT_NAME (optional): Custom name for your agent
     - AGENT_INSTRUCTIONS (optional): Custom instructions for your agent

## Running the Agent:

Run the following command in your terminal to start the agent:

```
 export OPENAI_API_KEY=your_api_key
 export AGENT_NAME="Joker"
 export AGENT_INSTRUCTIONS="You are a funny assistant who tells jokes and responds with humor."
 uv run main.py
```

- Type messages and get streamed responses from the agent
- Type 'exit' to quit
