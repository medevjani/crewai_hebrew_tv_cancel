import os
import json
from dotenv import load_dotenv

load_dotenv()

class TranscriptAgent:
    def __init__(self):
        self.output_dir = os.getenv("OUTPUT_DIR", "./outputs")
        os.makedirs(self.output_dir, exist_ok=True)
        self.log = []

    def add_entry(self, speaker, text):
        self.log.append({"speaker": speaker, "text": text})

    def save(self):
        path = os.path.join(self.output_dir, "transcript.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.log, f, ensure_ascii=False, indent=2)
        return path
