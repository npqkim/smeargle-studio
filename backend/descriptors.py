"""
descriptors.py
---------------
Maps raw audio feature values to human-readable descriptors
(e.g., fast tempo -> “energetic”, low brightness -> “warm”, etc.)

This module interprets audio features from analyze.py into words suitable
for prompt generation.
"""

GENRE_STYLES = {
    "rock": "edgy, bold, energetic, rebellious",
    "r&b": "smooth, expressive, soulful, elegant",
    "jazz": "improvisational, relaxed, artistic, vibrant",
    "edm": "futuristic, neon-lit, dynamic, high-energy",
    "lofi": "chill, cozy, muted colors, soft",
    "hip hop": "confident, rhythmic, urban, streetwise",
    "pop": "bright, upbeat, charismatic, approachable",
    "metal": "intense, dark, powerful, fierce",
    "blues": "soulful, moody, expressive, raw",
    "classical": "refined, graceful, harmonious, elegant",
    "reggae": "laid-back, colorful, warm, rhythmic",
    "country": "grounded, rustic, earthy, down-to-earth",
    "folk": "natural, storytelling, simple, heartfelt",
    "punk": "rebellious, raw, energetic, bold",
    "soul": "emotional, expressive, warm, intimate",
    "funk": "groovy, vibrant, playful, rhythmic",
    "techno": "mechanical, precise, futuristic, high-energy",
    "house": "smooth, pulsating, vibrant, rhythmic",
    "trap": "dark, edgy, intense, bold",
    "ambient": "ethereal, soft, atmospheric, dreamy"
}

def map_descriptors(features, genre="unknown"):
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

    descriptors = {}

    # Tempo
    tempo = min(max(features.get("tempo", 0) / 200, 0), 1)
    if tempo < 0.45:
        descriptors["tempo_desc"] = "slow"
    elif tempo < 0.65:
        descriptors["tempo_desc"] = "moderate"
    else:
        descriptors["tempo_desc"] = "fast"

    # Brightness
    brightness = min(max(features.get("brightness", 0) / 4000, 0), 1)
    if brightness < 0.25:
        descriptors["brightness_desc"] = "soft"
    elif brightness < 0.6:
        descriptors["brightness_desc"] = "balanced"
    else:
        descriptors["brightness_desc"] = "bright"

    # RMS / intensity
    rms = min(max(features.get("rms", 0), 0), 1)
    if rms < 0.2:
        descriptors["rms_desc"] = "soft"
    elif rms < 0.5:
        descriptors["rms_desc"] = "steady"
    elif rms < 0.8:
        descriptors["rms_desc"] = "lively"
    else:
        descriptors["rms_desc"] = "powerful"

    # Percussive
    perc = max(min(features.get("percussive_ratio", 0), 5), -5)
    if perc < 0:
        descriptors["percussive_desc"] = "smooth"
    elif perc < 1:
        descriptors["percussive_desc"] = "rhythmic"
    else:
        descriptors["percussive_desc"] = "edgy"

    # Genre
    genre_normalized = genre.strip().lower()
    descriptors["genre_style"] = GENRE_STYLES.get(genre_normalized, "unique, dynamic, expressive")

    # Flavor tags
    descriptors["flavor_tags"] = features.get("flavor_tags", [])

    return descriptors