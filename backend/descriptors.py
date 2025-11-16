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

    # Tempo -> agility / movement / combat style
    if tempo < 50:
        tempo_desc = "calm and deliberate, a strategist or healer"
    elif tempo < 80:
        tempo_desc = "graceful and measured, a skilled archer or scout"
    elif tempo < 120:
        tempo_desc = "alert and responsive, a versatile adventurer"
    elif tempo < 150:
        tempo_desc = "swift and aggressive, a frontline fighter"
    else:
        tempo_desc = "hyperactive and relentless, a berserker or speedster"

    # Brightness -> mood / aura
    if brightness < 1000:
        brightness_desc = "soft and intimate"
    elif brightness < 2000:
        brightness_desc = "gentle and wistful"
    elif brightness < 3000:
        brightness_desc = "vivid and bold"
    else:
        brightness_desc = "blazing and electrifying"

    # RMS -> emotional intensity / impact
    if rms < 0.05:
        rms_desc = "subtle and introspective"
    elif rms < 0.1:
        rms_desc = "expressive yet restrained"
    elif rms < 0.2:
        rms_desc = "powerful and commanding"
    else:
        rms_desc = "immense and overwhelming"

    # Percussive ratio -> rhythmic character / feel
    if percussive_ratio < 0.2:
        percussive_desc = "subtle, with gentle rhythmic undertones"
    elif percussive_ratio < 0.6:
        percussive_desc = "balanced and flowing rhythm"
    else:
        percussive_desc = "relentless, driving, and intense"

    return {
        "tempo_desc": tempo_desc,
        "brightness_desc": brightness_desc,
        "rms_desc": rms_desc,
        "percussive_desc": percussive_desc
    }
