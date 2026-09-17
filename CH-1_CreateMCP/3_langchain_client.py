from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
import sys

# Define the path to the MCP server script that will be started by the client.
mcp_server_script = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "1_first_mcpserver_stdio.py"
)

# Define the main asynchronous function that will create an instance of the MultiServerMCPClient,
# start the MCP server, and retrieve the available tools from the server.
async def main():
    client = MultiServerMCPClient(
    {
        # It is the configuration for the MCP server that will be started by the client
        "data_fetch_mcp_stdio": {

            # 'transport' specifies the transport method to communicate with the MCP server. 
            # In this case, it is set to "stdio", which means that the client will communicate with the server
            # using standard input and output streams.
            "transport": "stdio",

            # 'command' specifies the command to start the MCP server.
            # Here, it uses sys.executable to get the path of the current Python interpreter and
            # passes the path to the MCP server script as an argument.
            "command": sys.executable,

            # 'args' specifies the arguments to be passed to the command when starting the MCP server.
            "args": [mcp_server_script],
        }
    }
)

    # Start the MCP server using the client. This will launch the server process and establish communication.
    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())