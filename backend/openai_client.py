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

        print("📤 Sending prompt to OpenAI...")
        print(prompt)

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="720x720",
            response_format="b64_json"
        )

        print("✅ OpenAI responded successfully")

        # Decode base64 image
        img_data = response.data[0].b64_json
        img_bytes = base64.b64decode(img_data)
        
        with open(filename, "wb") as f:
            f.write(img_bytes)

        print(f"💾 Image saved: {filename}")
        return filename

    except Exception as e:
        print("❌ ERROR in generate_image():")
        print(e)
        return None
