"""
app.py
------
Main Flask backend application.

Routes:
- /analyze: Extracts audio features from uploaded file.
- /generate_art: Performs full pipeline:
      audio → features → descriptors → prompt → OpenAI → image_url

Handles form-data uploads from the frontend and returns JSON responses.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

from analyze import analyze_audio
from descriptors import map_descriptors
from prompt_builder import build_prompt
from openai_client import generate_image


def analyze_route():
    """
    Receive an uploaded audio file and return extracted audio features.

    Expects:
    - audio: file (in request.files)
    - genre: string (in request.form)

    Returns:
    - JSON: { "genre": str, "features": dict }
    """
    # implementation...


def generate_art():
    """
    Full pipeline endpoint.

    Steps:
    1. Read audio + genre from request
    2. Extract audio features
    3. Convert features → descriptive keywords
    4. Build final art prompt
    5. Call OpenAI to generate image
    6. Return image_url to frontend

    Returns:
    - JSON: {
        "prompt": str,
        "descriptors": dict,
        "image_url": str
      }
    """
    # implementation...
