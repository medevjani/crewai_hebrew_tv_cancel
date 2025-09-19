from agents.nikud_agent import NikudAgent
from agents.tts_agent import TTSAgent
from agents.stt_agent import STTAgent
from agents.sttext_agent import STTextAgent
from agents.customer_service_agent import CustomerServiceAgent
from agents.client_agent import ClientAgent
from agents.transcript_agent import TranscriptAgent
from tools.guardrails import guardrails

def run_cancellation_flow():
    nikud = NikudAgent()
    tts = TTSAgent()
    stt = STTAgent()
    sttext = STTextAgent()
    csr = CustomerServiceAgent()
    client = ClientAgent()
    transcript = TranscriptAgent()

    # Step 1: Client speaks
    client_text = client.speak()
    transcript.add_entry("Client", client_text)

    # Step 2: Add nikud
    client_nikud = nikud.add_nikud(client_text)

    # Step 3: Convert to voice
    client_voice_file = tts.speak(client_nikud, "outputs/client.wav")

    # Step 4: Transcribe (Whisper CPU)
    csr_input = stt.transcribe(client_voice_file)

    # Step 5: CSR responds
    #csr_response = csr.respond(csr_input)
    csr_response = csr.respond(client_text=client_text)
    csr_response = guardrails(csr_response)
    transcript.add_entry("CSR", csr_response)

    # Step 6: CSR response to speech
    csr_nikud = nikud.add_nikud(csr_response)
    csr_voice_file = tts.speak(csr_nikud, "outputs/csr.wav")

    # Step 7: Save transcript
    transcript_file = transcript.save()
   # return transcript_file, [client_voice_file, csr_voice_file]
    return transcript_file, [client_voice_file, csr_voice_file]
