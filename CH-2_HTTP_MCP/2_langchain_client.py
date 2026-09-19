from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
import sys

mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "CH-1_CreateMCP",
    "1_first_mcpserver_stdio.py"
)

async def main():

    connections = {
        # STDIO MCP server
        "data_fetch_mcp_stdio": {
            "transport": "stdio",
            "command": sys.executable,
            "args": [mcp_server_script],
        },

        # Streamable HTTP MCP server -> we added upon the 3_langchain_client.py file to add this connection to the client
        "data_fetch_mcp_http": {
            "transport": "streamable_http",
            "url": "http://localhost:8050/mcp",
        },
    }

    client = MultiServerMCPClient(connections)

    tools = await client.get_tools()

    print("Available tools:", tools)


if __name__ == "__main__":
    asyncio.run(main())