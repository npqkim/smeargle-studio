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
            output_format="png"
        )

        # Decode base64 image
        img_data = response.data[0].b64_json
        img_bytes = base64.b64decode(img_data)
        
        with open(filename, "wb") as f:
            f.write(img_bytes)

        print(f"Image saved to {filename}")
        return filename

    except Exception as e:
        print("Error generating image:", e)
        return None

if __name__ == "__main__":
    test_prompt = "A calm, lofi-inspired landscape with soft colors"
    generate_image(test_prompt)