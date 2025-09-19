import whisper
import os
from dotenv import load_dotenv

load_dotenv()

class STTAgent:
    def __init__(self):
        """
        Initialize Whisper STT agent using model size from .env
        Default is 'base' if not set.
        """
        model_size = os.getenv("WHISPER_MODEL_SIZE", "base")
        self.model = whisper.load_model(model_size, device="cpu")

    def transcribe(self, audio_file: str) -> str:
        """
        Transcribe an audio file into text (Hebrew supported).
        """
        result = self.model.transcribe(audio_file, language="he")
        return result["text"]
