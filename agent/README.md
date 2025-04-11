# How to Use

## Installation

1. Prerequisites:
   - install (uv)[https://docs.astral.sh/uv/getting-started/installation/]
   - the install the latest version of python `uv python install`

## Running the Agent:

```
 export OPENAI_API_KEY=your_api_key
 export AGENT_NAME="Joker"
 export AGENT_INSTRUCTIONS="You are a funny assistant who tells jokes and responds with humor."
 uv run agent/main.py
```

- Type messages and get streamed responses from the agent
- Type 'exit' to quit
