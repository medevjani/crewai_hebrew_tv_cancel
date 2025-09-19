import os
import json
from datetime import datetime
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

@tool("transcript_tool")
def transcript_tool(speaker: str, text: str):
    """Append conversation logs into transcript.json with timestamps."""
    log_entry = {
        "time": datetime.now().isoformat(),
        "speaker": speaker,
        "text": text
    }
    path = os.path.join(OUTPUT_DIR, "transcript.json")

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

    return path
