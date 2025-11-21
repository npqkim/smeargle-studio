# Smeargle Studio  
*(Project name subject to change)*

Smeargle Studio is an experimental tool that transforms an MP3 audio file into a fantasy-style AI-generated character. By analyzing the audio’s tempo, brightness, rms, percussive characteristics, the system produces a character image inspired by the sound.

---

## Features

- MP3 upload and processing  
- Audio analysis (tempo, brightness, rms, percussive ratio)  
- AI-generated fantasy character image  
- Optional JSON metadata export  
- Structured frontend and backend architecture  

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript 
- **Backend:** Python  
- **Audio Processing:** Librosa 
- **AI / Image Generation:** OpenAI API 

---

## Installation

Clone the repository:

```bash
git clone https://github.com/npqkim/smeargle-studio.git
cd smeargle-studio
```

## Local Usage Guide

This project contains a separate frontend and backend.  
To run Smeargle Studio locally, follow the steps below.

### 1. Requirements

- Python 3.9+  
- An OpenAI API key (place it in `backend/sk.py` or your environment variables)

Example (`backend/sk.py`):

```python
OPENAI_API_KEY = "your-api-key-here"
```
---

## 2. Backend Setup

Run the backend first — the frontend will not work without it.

1. Open a terminal and navigate to the backend directory:

   ```bash
   cd backend
   pip install -r libs.txt
   python app.py

## 3. Frontend Setup

The frontend is static (HTML, CSS, JS) and does not require Node or npm.
You can run it using any of the methods below.

### A. Open the HTML file directly

1. Open by double-clicking:

  ```bash
  frontend/index.html
  ```

### B. Open with VSCode Live Server:

1. Install the Live Server extension

2. Right-click index.html -> Open with Live Server

### C. Run a simple local server

1. Navigate to the frontend directory:

  ```bash
  cd frontend
  python -m http.server 8080 --bind 127.0.0.1
  ```

2. Visit:

  ```bash
  http://127.0.0.1:8080
  ```


