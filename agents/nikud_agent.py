from crewai import Agent
from tools.nikud_tool import add_nikud_tool

nikud_agent = Agent(
    role="Nikud Specialist",
    goal="Add Hebrew Nikud to improve pronunciation",
    backstory="Expert in Hebrew diacritics and phonetic enhancement.",
    tools=[add_nikud_tool],   # 👈 assigned here
    verbose=True
)
