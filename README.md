# CrewAI Hebrew TV Cancellation Demo

This project simulates a **customer support call in Hebrew** for cancelling a TV subscription, using CrewAI-style modular agents.

## Features
- **Client Agent**: asks to cancel TV subscription
- **CSR Agent**: polite response in Hebrew (via LiteLLM)
- **Nikud Agent**: adds diacritics with [Phonikud](https://github.com/thewh1teagle/phonikud)
- **TTS Agent**: converts Hebrew text to speech using [Chatterbox-TTS](https://github.com/resemble-ai/chatterbox)
- **STT Agent**: transcribes audio (stub/mock, replace with Whisper if needed)
- **Transcript Agent**: logs conversation to JSON
- **Guardrails**: filters unsafe responses
### Whisper STT
We use [OpenAI Whisper](https://github.com/openai/whisper) for transcription.  
It runs fully **offline on CPU**.  

You can set the model size in `.env`:
- `tiny` → fastest, lowest accuracy
- `base` → good balance (default)
- `small` → slower, more accurate
- `medium` → even slower, higher accuracy
- `large` → best accuracy, heavy on CPU

Example:
WHISPER_MODEL_SIZE=small

## Setup
```bash
git clone <repo>
cd crewai_hebrew_tv_cancel
cp .env.example .env   # edit with your API keys
#python -m venv venv
# Replace the path with the actual path to python3.10.exe if needed
py -3.11 -m venv .venv
# or, if py launcher is not available:
#C:\Path\To\Python310\python.exe -m venv venv
# python.exe -m pip install --force-reinstall numpy scipy 
.\.venv\Scripts\activate
#pip install numpy
pip install -r requirements.txt
cd chatterbox
pip install -e .