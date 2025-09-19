import os
from phonikud_onnx import Phonikud
from dotenv import load_dotenv

load_dotenv()

class NikudAgent:
    def __init__(self):
        model_path = os.getenv("NIKUD_MODEL_PATH")
        tokenizer_path = os.getenv("NIKUD_TOKENIZER_PATH")
        #self.model = Phonikud(model_path, tokenizer_path)
        self.model = Phonikud(model_path)

    def add_nikud(self, text: str) -> str:
        """Add Nikud (Hebrew diacritics) to text."""
        return self.model.add_diacritics(text)
