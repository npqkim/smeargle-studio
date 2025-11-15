"""
descriptors.py
---------------
Maps raw audio feature values to human-readable descriptors
(e.g., fast tempo → “energetic”, low brightness → “warm”, etc.)

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
    # implementation...
