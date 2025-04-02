"""
Cloudinary MCP Server

A server for optimizes and manages Cloudinary’s image hosting through MCP.
"""

from .server import mcp


def main() -> None:
    """Run the Cloudinary MCP server"""
    mcp.run()


__all__ = ['mcp', 'main']