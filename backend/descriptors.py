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

    # Tempo -> energy/motion
    if tempo < 50:
        tempo_desc = "slow and reflective"
    elif tempo < 80:
        tempo_desc = "gentle and flowing"
    elif tempo < 120:
        tempo_desc = "moderately lively"
    elif tempo < 150:
        tempo_desc = "energetic and dynamic"
    else:
        tempo_desc = "highly intense and fast-paced"

    # Brightness -> mood/light/color
    if brightness < 0.2:
        brightness_desc = "dark and moody"
    elif brightness < 0.4:
        brightness_desc = "soft and warm"
    elif brightness < 0.6:
        brightness_desc = "balanced and neutral"
    elif brightness < 0.8:
        brightness_desc = "bright and vibrant"
    else:
        brightness_desc = "very luminous and radiant"

    # RMS -> intensity/impact
    if rms < 0.01:
        rms_desc = "whisper-quiet and subtle"
    elif rms < 0.03:
        rms_desc = "soft and intimate"
    elif rms < 0.06:
        rms_desc = "moderately expressive"
    elif rms < 0.1:
        rms_desc = "loud and striking"
    else:
        rms_desc = "powerful and overwhelming"

    # Percussive ratio -> rhythm/texture
    if percussive_ratio < 0.2:
        percussive_desc = "smooth and flowing textures"
    elif percussive_ratio < 0.4:
        percussive_desc = "delicate rhythmic elements"
    elif percussive_ratio < 0.6:
        percussive_desc = "balanced rhythmic patterns"
    elif percussive_ratio < 0.8:
        percussive_desc = "strongly percussive and patterned"
    else:
        percussive_desc = "highly percussive and intricate textures"

    return {
        "tempo_desc": tempo_desc,
        "brightness_desc": brightness_desc,
        "rms_desc": rms_desc,
        "percussive_desc": percussive_desc
    }
