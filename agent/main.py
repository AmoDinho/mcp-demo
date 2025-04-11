"""
Agent using the OpenAI Agents Python library with MCP server support.
This agent can respond to user queries and perform tasks using tools from an MCP server.
"""

import os
import asyncio
import logging
from typing import Optional, List

from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings

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


async def interactive_chat(
    agent_name: str = "Assistant", 
    instructions: str = "You are a helpful assistant. Use the tools when appropriate.",
    api_key: Optional[str] = None,
    mcp_servers: Optional[List[MCPServer]] = None,
    require_tools: bool = False
) -> None:
    """
    Start an interactive chat session with the agent.
    
    Args:
        agent_name: Name for the agent
        instructions: Instructions for the agent's behavior
        api_key: OpenAI API key (if None, will use OPENAI_API_KEY environment variable)
        mcp_servers: List of MCP servers to connect to
        require_tools: Whether to require the agent to use tools
    """
    # Set API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Configure model settings based on tool requirements
    model_settings = ModelSettings(tool_choice="required" if require_tools else "auto")
    
    # Create the agent
    agent = Agent(
        name=agent_name,
        instructions=instructions,
        mcp_servers=mcp_servers or [],
        model_settings=model_settings,
    )
    
    # Generate a trace ID for tracking the conversation
    trace_id = gen_trace_id()
    print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
    
    # Start the trace for this conversation
    with trace(workflow_name=f"Interactive Chat with {agent_name}", trace_id=trace_id):
        # Simple conversation loop
        print(f"Interactive OpenAI Agent - {agent_name} (type 'exit' to quit)")
        print(f"Connected to {len(mcp_servers or [])} MCP servers")
        
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                break
                
            await process_agent_response(agent, user_input)


async def main():
    """Main function to run the agent with MCP server."""
    try:
        # Ensure API key is set
        if not os.environ.get("OPENAI_API_KEY"):
            logger.error("OPENAI_API_KEY environment variable not set")
            print("Please set your OPENAI_API_KEY environment variable")
            return
        
        # Get agent configuration from environment variables or use defaults
        agent_name = os.environ.get("AGENT_NAME", "Assistant")
        agent_instructions = os.environ.get("AGENT_INSTRUCTIONS", 
                                         "You are a helpful assistant. Use the available tools when appropriate to answer questions.")
        
        # Get MCP server configuration from environment variables
        mcp_server_url = os.environ.get("MCP_SERVER_URL", "http://localhost:3001/sse")
        require_tools = os.environ.get("REQUIRE_TOOLS", "false").lower() == "true"
        
        # Connect to MCP server
        async with MCPServerSse(
            name="SSE Python Server",
            params={
                "url": mcp_server_url,
            },
        ) as mcp_server:
            logger.info(f"Connected to MCP server at {mcp_server_url}")
            
            # Start interactive chat with MCP server
            await interactive_chat(
                agent_name=agent_name,
                instructions=agent_instructions,
                mcp_servers=[mcp_server],
                require_tools=require_tools
            )
    
    except Exception as e:
        logger.exception("An error occurred")
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
