import csv
import os
import httpx
from dotenv import load_dotenv, set_key

# Ensure .env exists with necessary keys
ENV_FILE = ".env"
DEFAULTS = {
    "ELEVENLABS_API_KEY": "your-elevenlabs-api-key",
    "ELEVENLABS_VOICE_ID": "your-elevenlabs-voice-id",
}

if not os.path.exists(ENV_FILE):
    with open(ENV_FILE, "w") as f:
        for key, value in DEFAULTS.items():
            f.write(f"{key}={value}\n")
    print(f"Created {ENV_FILE}, please fill in your API details.")
    exit()

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

if not API_KEY or not VOICE_ID:
    print("Missing API credentials in .env. Fill in and rerun.")
    exit()

OUTPUT_DIR = "voice"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_speech(text, output_path):
    """Send text to ElevenLabs and save the response as an audio file."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": API_KEY}
    json_data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }

    with httpx.Client() as client:
        response = client.post(url, headers=headers, json=json_data)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Generated: {output_path}")
    else:
        print(f"Failed for {output_path}: {response.text}")


# Process dialogue.tab
with open("dialogue.tab", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        if len(row) < 3:
            continue

        id_, speaker, text = row[:3]

        if speaker.lower() == "m":
            output_path = os.path.join(OUTPUT_DIR, f"{id_}.ogg")

            if not os.path.exists(output_path):  # Skip if already exists
                generate_speech(text, output_path)
