import os 
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio


# Path to the MCP server script
mcp_server_script = os.path.join((os.path.dirname(os.path.abspath(__file__))),"1_first_mcpserver_stdio.py")
print(mcp_server_script)

# Create Server Parameters
server_params = StdioServerParameters(
    # we specify the command to run the MCP server script using Python
    command="python",
    # we specify the arguments(here it is an address) for the Python command, it is in string format, as it might be an object
    args=[str(mcp_server_script)],
    # we specify the environment variables for the MCP server process, it is in dictionary format
    env={}
)


# Create a Client Session
async def main():
    # Use the stdio_client context manager to connect to the MCP server
    # The stdio_client context manager takes the server parameters and establishes a connection to the MCP server using standard input/output.
    async with stdio_client(server_params) as (read,write):

        # (creates the MCP session) Create a ClientSession using the read and write streams from the stdio_client context manager
        async with ClientSession(read,write) as session:

            # Initialize the session to prepare for tool calls
            await session.initialize()

            # (sends an MCP tools/list request to the server) Fetch the tools available on the MCP server using the list_tools method of the ClientSession.
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Use the fetch tool to fetch data from the MCP server using the call_tool method of the ClientSession. 
            result = await session.call_tool("process",arguments={"path": "/path/to/data"})
            print("\n\nResult:", result)


if __name__ == "__main__":
    asyncio.run(main())