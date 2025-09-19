from litellm import transcription
import os
from dotenv import load_dotenv

load_dotenv()

class STTextAgent:
    def __init__(self):
        """
        Initialize Whisper STT agent using model size from .env
        Default is 'base' if not set.
        """

    def transcribe(self, audio_file: str) -> str:
        """
        Transcribe an audio file into text (Hebrew supported).
        """
        audio_file = open(audio_file, "rb")

        response = transcription(model="whisper-1", file=audio_file)
        return response
