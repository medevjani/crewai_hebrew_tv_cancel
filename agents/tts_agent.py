from crewai import Agent
from tools.tts_tool import tts_tool

tts_agent = Agent(
    role="Text-to-Speech Specialist",
    goal="Convert Hebrew text to natural speech",
    backstory="Generates realistic Hebrew voices from text input.",
    tools=[tts_tool],   # 👈 assigned here
    verbose=True
)
