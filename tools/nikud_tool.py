import os
from phonikud_onnx import Phonikud
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

model = Phonikud(
    os.getenv("NIKUD_MODEL_PATH")
    #os.getenv("NIKUD_TOKENIZER_PATH")
)

@tool("add_nikud_tool")
def add_nikud_tool(text: str) -> str:
    """Add Nikud to Hebrew text."""
    return model.add_diacritics(text)
