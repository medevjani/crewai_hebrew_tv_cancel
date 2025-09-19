from crewai import Agent

client_agent = Agent(
    role="Client",
    goal="Cancel their television subscription",
    backstory="Wants to stop paying for TV and get confirmation of cancellation.",
    tools=[],   # 👈 no tools, just fixed dialogue
    verbose=True
)
