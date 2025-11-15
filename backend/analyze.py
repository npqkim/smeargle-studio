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
    # Load audio from in-memory bytes
    audio_buffer = io.BytesIO(audio_bytes)
    signal, sr = sf.read(audio_buffer, dtype="float32")

    # Convert stereo → mono
    if len(signal.shape) > 1:
        signal = np.mean(signal, axis=1)

    # Tempo
    tempo, _ = librosa.beat.beat_track(y=signal, sr=sr)

    # Brightness (spectral centroid)
    spectral_centroid = librosa.feature.spectral_centroid(y=signal, sr=sr)
    brightness = float(np.mean(spectral_centroid))

    # RMS loudness
    rms = librosa.feature.rms(y=signal)
    rms_value = float(np.mean(rms))

    # Harmonic/Percussive Energy Ratio 
    harmonic, percussive = librosa.effects.hpss(signal)
    percussive_ratio = float(
        np.mean(percussive) / (np.mean(harmonic) + 1e-6)
    )  # avoid divide-by-zero error

    return {
        "tempo": float(tempo),
        "brightness": brightness,
        "rms": rms_value,
        "percussive_ratio": percussive_ratio
    }