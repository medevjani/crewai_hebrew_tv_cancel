from crewai import Agent
from tools.stt_tool import stt_tool

stt_agent = Agent(
    role="Speech-to-Text Specialist",
    goal="Transcribe Hebrew speech to text",
    backstory="Uses Whisper to accurately transcribe Hebrew audio on CPU.",
    tools=[stt_tool],   # 👈 assigned here
    verbose=True
)
