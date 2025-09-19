import os
import torchaudio
from dotenv import load_dotenv
from chatterbox.tts import ChatterboxTTS
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

load_dotenv()

class TTSAgent:
    def __init__(self):
        self.device = os.getenv("CHATTERBOX_DEVICE", "cpu")
        model_name = os.getenv("CHATTERBOX_MODEL", "chatterbox-tts:latest")
        #self.model = ChatterboxTTS.from_pretrained(device=self.device)
        self.model = ChatterboxMultilingualTTS.from_pretrained(device=self.device)

    def speak(self, text: str, output_file: str):
        """Convert Hebrew text to speech and save as wav."""
        audio = self.model.generate(text, language_id="he")
        torchaudio.save(output_file, audio, 22050)
        return output_file