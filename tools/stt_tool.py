from litellm import transcription
import os
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

@tool("stt_tool")
def stt_tool(audio_file: str) -> str:
    """
    Transcribe an audio file into text (Hebrew supported).
    """
    audio_file = open(audio_file, "rb")

    response = transcription(model="whisper-1", file=audio_file)
    return response
