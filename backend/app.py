"""
app.py
------
Main Flask backend application.

Routes:
- /analyze: Extracts audio features from uploaded file.
- /generate_art: Performs full pipeline:
      audio -> features -> descriptors -> prompt -> OpenAI -> image_url

Handles form-data uploads from the frontend and returns JSON responses.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

from analyze import analyze_audio
from descriptors import map_descriptors
from prompt_builder import build_prompt
from openai_client import generate_image

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_route():
    """
    Receive an uploaded audio file and return extracted audio features.

    Expects:
    - audio: file (in request.files)
    - genre: string (in request.form)

    Returns:
    - JSON: { "genre": str, "features": dict }
    """
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    genre = request.form.get("genre", "unknown")

    audio_bytes = audio_file.read()

    # get features
    features = analyze_audio(audio_bytes)

    return jsonify({
        "genre": genre,
        "features": features
    })


def generate_art():
    """
    Full pipeline endpoint.

    Steps:
    1. Read audio + genre from request
    2. Extract audio features
    3. Convert features -> descriptive keywords
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
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    genre = request.form.get("genre", None)

    if not genre:
        return jsonify({"error": "Genre is missing"}), 400

    audio_bytes = audio_file.read()

    # 1) Extract numeric features
    features = analyze_audio(audio_bytes)

    # 2) Convert numeric features -> English descriptors
    print("Raw audio features:", features)
    descriptors = map_descriptors(features)

    # 3) Build OpenAI prompt string
    prompt = build_prompt(genre, descriptors)

    # 4) Call OpenAI and retrieve generated image URL
    image_url = generate_image(prompt)

    return jsonify({
        "prompt": prompt,
        "descriptors": descriptors,
        "image_url": image_url
    })

@app.route("/generate_art", methods=["POST"])
def generate_art_route():
    """
    Flask route wrapping the generate_art function.
    This exposes the full pipeline to the frontend.
    """
    return generate_art()

@app.route("/", methods=["GET"])
def home():
    return "Smeargle Studio Backend Running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
