import requests
import webbrowser

# URL of your running Flask backend
url = "http://127.0.0.1:5001/generate_art"

# Path to your audio file
audio_file_path = "test.mp3"

# Genre of the music
genre = "R&B"

# Open the audio file in binary mode
with open(audio_file_path, "rb") as f:
    audio_bytes = f.read()  # Read the audio file

# DEBUG: Call analyze_audio locally if possible (requires import) or just print size
# If you want to call analyze_audio here, make sure to import it:
# from analyze import analyze_audio
# features = analyze_audio(audio_bytes)
# print("Raw audio features:", features)

# Send POST request to backend
files = {"audio": open(audio_file_path, "rb")}
data = {"genre": genre}

response = requests.post(url, files=files, data=data)

# Check if request was successful
if response.status_code == 200:
    result = response.json()
    print("Prompt:", result.get("prompt"))
    print("Descriptors:", result.get("descriptors"))
    print("Generated Image URL:", result.get("image_url"))

    # Optional: open the generated image in the default web browser
    image_url = result.get("image_url")
    if image_url:
        webbrowser.open(image_url)
else:
    print(f"Error {response.status_code}: {response.text}")
