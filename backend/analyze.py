"""
analyze.py
----------
Handles audio feature extraction using librosa.
Given raw audio bytes, this module loads the audio, converts it to mono,
and computes core musical features: tempo, brightness, RMS energy,
and percussive ratio.
"""

import librosa
import soundfile as sf
import numpy as np
import io


def analyze_audio(audio_bytes):
    """
    Analyze the provided audio bytes and return extracted music features.

    Parameters:
    - audio_bytes (bytes): Raw audio data from an uploaded file.

    Returns:
    - dict: {
        "tempo": float,
        "brightness": float,
        "rms": float,
        "percussive_ratio": float
      }
    """
    # implementation...
