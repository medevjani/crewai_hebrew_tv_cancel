from crewai import Task

from agents.client_agent import client_agent
from agents.nikud_agent import nikud_agent
from agents.tts_agent import tts_agent
from agents.stt_agent import stt_agent
from agents.customer_service_agent import customer_service_agent
from agents.transcript_agent import transcript_agent

def build_cancellation_tasks():
    return [
        Task(
            description="Client initiates a request to cancel their television subscription.",
            agent=client_agent,
            expected_output="Raw Hebrew text of the cancellation request (without Nikud)."
        ),
        Task(
            description="Add Hebrew Nikud to the client’s request to improve pronunciation.",
            agent=nikud_agent,
            expected_output="Hebrew text with Nikud annotations."
        ),
        Task(
            description="Convert the Nikud-annotated client request into a Hebrew audio file.",
            agent=tts_agent,
            expected_output="File path to generated client speech WAV file."
        ),
        Task(
            description="Transcribe the client’s Hebrew audio request back into plain text.",
            agent=stt_agent,
            expected_output="Plain Hebrew transcription of the client’s spoken cancellation request."
        ),
        Task(
            description="The Customer Service Representative responds politely to the cancellation request.",
            agent=customer_service_agent,
            expected_output="Hebrew text response from CSR, ensuring politeness and clarity."
        ),
        Task(
            description="Add Hebrew Nikud to the CSR’s response and convert it to speech.",
            agent=tts_agent,
            expected_output="File path to generated CSR speech WAV file."
        ),
        Task(
            description="Log the full conversation into a transcript file with timestamps. It should include client request's raw hebrew text, nikud agent output for client request, the customer service agent's response in plain raw hebrew text and nikud agent's output for customer service agent's response",
            agent=transcript_agent,
            expected_output="Path to updated transcript.json containing all conversation turns."
        )
    ]
