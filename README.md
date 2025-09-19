# CrewAI Hebrew TV Cancellation Demo

This project simulates a **customer support call in Hebrew** for cancelling a TV subscription, using CrewAI-style modular agents.

# Prerequisites
- [ffmpeg](https://www.ffmpeg.org/download.html) tool to be installed in local and exe path to be added in the path variable
- [phonikud-1.0.int8.onnx](https://huggingface.co/thewh1teagle/phonikud-onnx) model file is not part of the package since it is very large in size. The same has to be downloaded and added inside models folder
- virtual environment to be created on python version=3.11
- open ai api keys, to be configured in .env file

## Features
- **Client Agent**: asks to cancel TV subscription
- **CSR Agent**: polite response in Hebrew (via LiteLLM)
- **Nikud Agent**: adds diacritics with [Phonikud](https://github.com/thewh1teagle/phonikud)
- **TTS Agent**: converts Hebrew text to speech using [Chatterbox-TTS](https://github.com/resemble-ai/chatterbox) . Since multilingual support was not working properly in CPU mode, chatterbox code is locally downloaded, updated and used as part of the solution
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
pip install -r requirements.txt
cd chatterbox
pip install -e .
cd..