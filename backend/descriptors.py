"""
descriptors.py
---------------
Maps raw audio feature values to human-readable descriptors
(e.g., fast tempo -> “energetic”, low brightness -> “warm”, etc.)

This module interprets audio features from analyze.py into words suitable
for prompt generation.
"""


def map_descriptors(features):
    """
    Convert audio feature values into descriptive terms.

    Parameters:
    - features (dict): {
        "tempo": float,
        "brightness": float,
        "rms": float,
        "percussive_ratio": float
    }

    Returns:
    - dict: {
        "tempo_desc": str,
        "brightness_desc": str,
        "rms_desc": str,
        "percussive_desc": str
    }
    """
    tempo = features.get("tempo", 0)
    brightness = features.get("brightness", 0)
    rms = features.get("rms", 0)
    percussive_ratio = features.get("percussive_ratio", 0)

    # RMS -> emotional tone of the character
    if rms < 0.05:
        rms_desc = "emotionally reserved with a calm, collected presence"
    elif rms < 0.1:
        rms_desc = "soft-spoken but emotionally aware and thoughtful"
    elif rms < 0.2:
        rms_desc = "passionate and expressive, emotions close to the surface"
    else:
        rms_desc = "intense, volatile, and overwhelmingly emotional"

    # Brightness -> color scheme vividness / aura
    if brightness < 1000:
        brightness_desc = "muted, low-saturation colors with a soft, understated palette"
    elif brightness < 2000:
        brightness_desc = "gentle mid-tone colors with subtle accents"
    elif brightness < 3000:
        brightness_desc = "vivid, high-contrast colors with bold highlights"
    else:
        brightness_desc = "hyper-saturated, electrifying colors that almost glow"

    # Percussive ratio -> fashion style: grungy ↔ light/airy
    if percussive_ratio < 0.2:
        percussive_desc = "light, airy fashion with flowing fabrics and clean lines"
    elif percussive_ratio < 0.6:
        percussive_desc = "balanced, modern streetwear with a mix of soft and structured pieces"
    else:
        percussive_desc = "grungy, layered fashion with worn textures, rips, and metallic details"

    # Tempo -> combat strength ↔ intellect/nerdy axis
    if tempo < 60:
        tempo_desc = (
            "a highly intellectual, bookish character who relies on strategy and knowledge "
            "far more than physical strength"
        )
    elif tempo < 90:
        tempo_desc = (
            "a clever tactician who balances mental sharpness with just enough physical skill "
            "to hold their own"
        )
    elif tempo < 130:
        tempo_desc = (
            "a capable fighter with quick reactions, guided by instinct as much as thought"
        )
    elif tempo < 160:
        tempo_desc = (
            "a fierce close-combat specialist who solves problems head-on rather than with careful planning"
        )
    else:
        tempo_desc = (
            "a hyper-aggressive powerhouse who charges in first and thinks later"
        )

    # Combined character descriptor for prompt generation
    character_descriptor = (
        f"A fictional character who is {rms_desc}. "
        f"They are depicted with {brightness_desc}, wearing {percussive_desc}. "
        f"They are {tempo_desc}."
    )

    return {
        "tempo_desc": tempo_desc,
        "brightness_desc": brightness_desc,
        "rms_desc": rms_desc,
        "percussive_desc": percussive_desc
    }
