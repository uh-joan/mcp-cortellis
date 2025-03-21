"""
Cortellis MCP Server main entry point.
"""
from mcp.server.fastmcp import FastMCP
from . import search_drugs, explore_ontology

def main():
    # Initialize the MCP server
    mcp = FastMCP("Cortellis MCP")
    
    # Register tools
    mcp.tool()(search_drugs)
    mcp.tool()(explore_ontology)
    
    print("Initializing Cortellis MCP Server...")
    # Start the server - this will block and listen for JSON-RPC messages
    mcp.run()

if __name__ == "__main__":
    main() 