import os
import torchaudio
from chatterbox.tts import ChatterboxTTS
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

chatterbox_device = os.getenv("CHATTERBOX_DEVICE", "cpu")
model_name = os.getenv("CHATTERBOX_MODEL", "chatterbox-tts:latest")
#model = ChatterboxTTS.from_pretrained(device=device)
model = ChatterboxMultilingualTTS.from_pretrained(device=chatterbox_device)

@tool("tts_tool")
def tts_tool(text: str, output_file: str) -> str:
    """Convert Hebrew text to speech and save as wav."""
    audio = model.generate(text, language_id="he")
    torchaudio.save(output_file, audio, 22050)
    return output_file
