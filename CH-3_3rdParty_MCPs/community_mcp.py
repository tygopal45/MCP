from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os 


async def main():

    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

    # MCP Server Config (JSON)
    {
        "data_fetch_mcp_stdio":{
            "transport": "stdio",
            # diretly uses uvx to fetch the duckduckgo-mcp-server which is global 
            "command": "uvx",
            # argument just after command, which is the name of the MCP server to run
            "args": ["duckduckgo-mcp-server"]
        }

    }
    )

    # List the tools
    tools = await client.get_tools()
    # print("Available tools:", len(tools))
    for tool in tools:
        print("Available tool:", tool.name)
    

    # Call a tool (XXXX Not working  Wrong way to call the tool using client.invoke, use tool.ainvoke instead)
    # result = await client.invoke("search", {"query": "What is the capital of France?"})
    # print("Tool result:", result)

    # Once the client is initialized, you can also directly call the tool using the tool object
    # Tool object which are Native to LangChain can be used directly to invoke the tool

    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"query": "What is the capital of France?"})
    print("Tool result:", result)


if __name__ == "__main__":
    asyncio.run(main())
