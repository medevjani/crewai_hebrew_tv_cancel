from crewai import Agent
from tools.guardrails_tool import guardrails_tool
from tools.transcript_tool import transcript_tool

customer_service_agent = Agent(
    role="Customer Service Representative",
    goal="Help client cancel their TV subscription politely",
    backstory="Trained to manage cancellations and retention while staying polite.",
    tools=[guardrails_tool, transcript_tool],   # 👈 CSR uses both
    verbose=True
)
