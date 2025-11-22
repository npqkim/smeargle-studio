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
    genre_style = descriptors.get("genre_style", "")

    prompt_parts = []

    # Character personality based on genre and tempo
    genre_style = descriptors.get("genre_style", "")
    tempo_desc = descriptors.get("tempo_desc", "")
    if genre_style or tempo_desc:
        prompt_parts.append(
            f"Create a fictional character who is {genre_style}, with a {tempo_desc} demeanor."
        )

    # Visual appearance based on brightness
    brightness_desc = descriptors.get("brightness_desc", "")
    if brightness_desc:
        prompt_parts.append(
            f"Their appearance features {brightness_desc} colors, lighting, and atmosphere."
        )

    # Energy / emotional intensity
    rms_desc = descriptors.get("rms_desc", "")
    if rms_desc:
        prompt_parts.append(
            f"They exude {rms_desc} energy, reflected in their posture and expression."
        )

    # Style / movement
    percussive_desc = descriptors.get("percussive_desc", "")
    if percussive_desc:
        prompt_parts.append(
            f"Their movements and style are {percussive_desc}."
        )

    # Optional flavor tags
    flavor_tags = descriptors.get("flavor_tags", [])
    if flavor_tags:
        tags = ", ".join(flavor_tags)
        prompt_parts.append(f"Include extra details: {tags}.")

    # Artistic and combat details
    prompt_parts.append(
        "Describe their clothing, armor, accessories, or symbolic motifs, "
        "and show personality through their stance, weapons, or abilities. "
        "Include imaginative and grounded elements for a unique, dynamic, and visually striking character."
    )

    # Optional color guidance
    prompt_parts.append(
        "Use balanced colors and subtle highlights for a harmonious visual."
    )

    # Combine all parts into one prompt
    return " ".join(prompt_parts)