"""
openai_client.py
----------------
Handles communication with the OpenAI API.
Sends the constructed image prompt and returns the generated image URL.
"""

from openai import OpenAI
from sk import OPENAI_API_KEY
import base64

client = OpenAI(api_key=OPENAI_API_KEY)
def generate_image(prompt, filename = "output.png"):
    """
    Send an image-generation prompt to the OpenAI API.

    Parameters:
    - prompt (str): Text prompt describing the desired landscape art.

    Returns:
    - str: URL pointing to the generated image.
    """
    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024",
            n=1
        )

        # Get base64 image data
        image_b64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_b64)

        # Save to file
        with open(filename, "wb") as f:
            f.write(image_bytes)
        return filename

    except Exception as e:
        return None
