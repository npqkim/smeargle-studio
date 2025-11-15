"""
prompt_builder.py
-----------------
Builds the final descriptive text prompt used for OpenAI image generation.

Takes the musical genre and descriptor keywords and formats them into
a coherent landscape-art prompt string.
"""


def build_prompt(genre, descriptors):
    """
    Construct a detailed prompt for the image generator.

    Parameters:
    - genre (str): User-selected genre (e.g., lofi, edm, jazz).
    - descriptors (dict): Mapping of audio feature descriptors.

    Returns:
    - str: Final descriptive prompt for image generation.
    """
    # implementation...
