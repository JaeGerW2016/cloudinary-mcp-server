from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("cloudinary-mcp-server")

from urllib.parse import urlparse
import os
import cloudinary
from cloudinary import uploader

# config Cloudinary
cloudinary.config(
  cloudinary_url=os.environ['CLOUDINARY_URL']
)

@mcp.tool()
async def upload_image(image: str) -> str:
    """Uploads an image to Cloudinary.

    Args:
        image: Image file path or url of the image to upload.

    Returns:
        str: Secure URL of the uploaded image on Cloudinary CDN.
    """
    upload_result = uploader.upload(
        image,
        transformation=[
            {'quality': 'auto',
             'fetch_format':'auto'}
        ]
    )
    return upload_result['secure_url']


if __name__ == "__main__":
    import asyncio
    path = asyncio.run(upload_image('https://youjb.com/images/2025/04/02/shell-operator-small-logo63673460b9ae9ab4.png'))
    print(path)