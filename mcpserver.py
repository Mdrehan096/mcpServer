from mcp.server.mcpserver import MCPServer

mcp = MCPServer("rehan kitchen")

@mcp.tool()
def padho_add(a: int , b : int) -> int:
    """ add the two number using the padho calculator"""  
    return a + b + 100                        

if __name__ == "__main__":
    mcp.run()