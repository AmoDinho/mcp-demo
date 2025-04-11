# How to Use

## Installation

1. Prerequisites:
   - install (uv)[https://docs.astral.sh/uv/getting-started/installation/]
   - the install the latest version of python `uv python install`
   - Set up environment variables:
     - OPENAI_API_KEY: Your OpenAI API key
     - AGENT_NAME (optional): Custom name for your agent
     - AGENT_INSTRUCTIONS (optional): Custom instructions for your agent

## Running the Agent:

```
 export OPENAI_API_KEY=your_api_key
 export AGENT_NAME="Joker"
 export AGENT_INSTRUCTIONS="You are a funny assistant who tells jokes and responds with humor."
 python agent/main.py
```

- Type messages and get streamed responses from the agent
- Type 'exit' to quit
