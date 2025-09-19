from crewai import Agent
from tools.transcript_tool import transcript_tool

transcript_agent = Agent(
    role="Transcript Logger",
    goal="Log every speaker turn with timestamp",
    backstory="Keeps an organized JSON transcript of the entire call.",
    tools=[transcript_tool],   # 👈 assigned here
    verbose=True
)
