import asyncio

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

from mcp_use import MCPAgent, MCPClient
import os


async def ru_memory_chat():

    load_dotenv()   
    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    config_file = 'browser_mcp.json'

    print("Starting Groq chat...")

    client = MCPClient.from_config_file(config_file)
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.1)

    agent  = MCPAgent(llm=llm,
        client=client,
        memory_enabled=True)
    
    print("Interactive MCP chat session started.")

    try: 
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Memory cleared.")
                continue
            
            print("\nAssistant:", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(f"Agent: {response}")
            except Exception as e:
                print(f"Error during chat: {e}")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()
            print("Client connection closed.")

if __name__ == "__main__":
    asyncio.run(ru_memory_chat())