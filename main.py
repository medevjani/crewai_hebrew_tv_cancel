from crewai import Crew
from tasks.cancellation_task import build_cancellation_tasks
from agents.client_agent import client_agent
from agents.customer_service_agent import customer_service_agent
from agents.nikud_agent import nikud_agent
from agents.tts_agent import tts_agent
from agents.stt_agent import stt_agent
from agents.transcript_agent import transcript_agent

if __name__ == "__main__":
    agents = [
        client_agent,
        customer_service_agent,
        nikud_agent,
        tts_agent,
        stt_agent,
        transcript_agent
    ]
    tasks = build_cancellation_tasks()

    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

    #result = crew.run()
    result = crew.kickoff()
    print("Final result:", result)
