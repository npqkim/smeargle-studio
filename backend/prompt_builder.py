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
        f"Create a {genre}-inspired artwork that is {tempo_desc}, "
        f"{brightness_desc}, {rms_desc}, and features {percussive_desc}. "
        "Use vivid imagery and artistic interpretation to reflect the audio characteristics."
    )

    return prompt
