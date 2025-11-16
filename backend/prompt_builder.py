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
    tempo_desc = descriptors.get("tempo_desc", "")
    brightness_desc = descriptors.get("brightness_desc", "")
    rms_desc = descriptors.get("rms_desc", "")
    percussive_desc = descriptors.get("percussive_desc", "")

    prompt = (
    f"Create a {genre}-inspired fictional character who embodies {tempo_desc}. "
    f"They possess a {brightness_desc} presence, carry the {rms_desc} weight of their power, "
    f"and demonstrate {percussive_desc} in their fighting style, movements, or magical abilities. "
    "Include rich details about their armor, weapons, magical skills, and personality traits."
    )

    return prompt