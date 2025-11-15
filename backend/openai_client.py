"""
openai_client.py
----------------
Handles communication with the OpenAI API.
Sends the constructed image prompt and returns the generated image URL.
"""

from openai import OpenAI


def generate_image(prompt):
    """
    Send an image-generation prompt to the OpenAI API.

    Parameters:
    - prompt (str): Text prompt describing the desired landscape art.

    Returns:
    - str: URL pointing to the generated image.
    """
    # implementation...
