"""
Simple agent using the OpenAI Agents Python library.
This agent can respond to user queries and perform basic tasks.
"""

import os
import asyncio
import logging
from typing import Optional

from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def process_agent_response(agent: Agent, user_input: str) -> None:
    """
    Process a user input, send it to the agent, and stream the response.
    
    Args:
        agent: The OpenAI agent to use
        user_input: The user's message
    """
    print("\nAgent is thinking...")
    result = Runner.run_streamed(agent, input=user_input)
    
    print("\nAgent: ", end="", flush=True)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
    print()  # Add a newline after the agent's response


async def interactive_chat(agent_name: str = "Assistant", 
                          instructions: str = "You are a helpful assistant.",
                          api_key: Optional[str] = None) -> None:
    """
    Start an interactive chat session with the agent.
    
    Args:
        agent_name: Name for the agent
        instructions: Instructions for the agent's behavior
        api_key: OpenAI API key (if None, will use OPENAI_API_KEY environment variable)
    """
    # Set API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        
    # Create the agent
    agent = Agent(
        name=agent_name,
        instructions=instructions,
    )
    
    # Simple conversation loop
    print(f"Simple OpenAI Agent - {agent_name} (type 'exit' to quit)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
            
        await process_agent_response(agent, user_input)


async def main():
    """Main function to demonstrate the agent."""
    try:
        # Ensure API key is set
        if not os.environ.get("OPENAI_API_KEY"):
            logger.error("OPENAI_API_KEY environment variable not set")
            print("Please set your OPENAI_API_KEY environment variable")
            return
        
        # Get agent configuration from environment variables or use defaults
        agent_name = os.environ.get("AGENT_NAME", "Assistant")
        agent_instructions = os.environ.get("AGENT_INSTRUCTIONS", 
                                           "You are a helpful assistant who provides clear, concise answers.")
        
        # Start interactive chat
        await interactive_chat(agent_name, agent_instructions)
    
    except Exception as e:
        logger.exception("An error occurred")
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
