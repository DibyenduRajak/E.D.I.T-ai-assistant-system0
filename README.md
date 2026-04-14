# E.D.I.T-ai-assistant-system


🧠 Core Architecture Overview


🔷 1. Main Brain (Orchestrator AI)


This is the decision engine.


Responsibilities:


Understand user intent
Decide which model/tool to call
Manage task flow
Maintain conversation memory


👉 Recommended:


Run via Ollama
Model options:
gemma:3 (fast + structured)
llama3 (better reasoning)



🔷 2. Worker Models (Specialized AIs)



You’ll run 3 local models, each optimized for a domain:


🟢 Model 1 – Conversational AI

General chat / reasoning

Handles user interaction

🔵 Model 2 – Code / System AI

Writes scripts

Executes commands

Controls OS / Docker / server

🟣 Model 3 – Vision / Audio AI

Image understanding

Voice processing (Whisper / TTS)



👉 Tools:



Speech-to-text: Whisper
TTS: Coqui / Piper

Vision: LLaVA or similar

🔷 3. Task Router (Middleware Layer)



This is critical. Your “brain” should NOT directly do everything.



You need a routing layer:



User Input → Brain → Task Router → Selected Model → Output → Brain → Response

⚙️ Suggested Tech Stack

Backend

Python (FastAPI)

Async orchestration


AI Runtime

Ollama

Memory


Vector DB:

FAISS (local)


ChromaDB

Voice

Whisper (input)

Piper (output)

UI (optional)

Electron / Web dashboard (like your E.D.D.Y UI)

🧩 System Flow (Step-by-Step)
1. User Input
Text OR voice
2. Brain AI Processes Intent

Example:

"Start my minecraft server and check RAM usage"
3. Brain Decides:
Needs system control → send to Code AI
4. Code AI Executes:
Runs shell/docker commands
5. Brain Collects Output
Formats response



++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<br>
▶️  RUN SYSTEM<br>

python -m venv venv<br>
venv\Scripts\activate<br>
pip install -r requirements.txt<br>

uvicorn api.server:app --port 8000<br>

python main.py<br>

Open UI: ui/index.html<br>

⚠️ FINAL SETUP NOTES<br>
🔴 Download Piper Voice<br>

Place in root:<br>

en_US-lessac-medium.onnx<br>
🔴 Stable Diffusion First Run<br>
Will download ~5GB<br>
Needs GPU (recommended)<br>
🔴 Mic Fix (Windows)<br>
pip install pipwin<br>
pipwin install pyaudio<br>


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/689bfe19-f9c9-43f5-a529-a09040d036d5" />

