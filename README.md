# 🧠 MindMate AI API

MindMate AI is a conversational AI backend designed for emotionally supportive dialogue and realistic voice responses.
It integrates large language models and neural text-to-speech to provide a natural chat and voice experience.

The backend is built using FastAPI and integrates AI models through NVIDIA NIM APIs and Google AI services.

## 🖥️ Deployment

- deployed: <https://mindmate-ai-api.onrender.com>


open api docs: 
- <https://mindmate-ai-api.onrender.com/docs>

 or

- <https://mindmate-ai-api.onrender.com/scalar_docs>


## ✨ Features

- 💬 AI chat responses

- 🧠 Automatic conversation name generation

- 🔊 Neural text-to-speech voice responses

- ⚡ Fast REST API

- 🩺 Health monitoring endpoint

- 🔁 Backup LLM fallback system

## 🏗 Architecture

```text
Frontend
   ↓
MindMate API (FastAPI)
   ↓
Primary LLM → NVIDIA NIM (OpenAI's GPT OSS 120B)
   ↓
Fallback LLM → Gemini 2.5 Flash Lite
   ↓
Text Response
   ↓
Magpie TTS
   ↓
.wav Voice Output
```

## ▶️ How to Run MindMate AI

Follow these steps to run the backend locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/mindmate-ai.git
cd mindmate-ai
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

MindMate uses **Magpie TTS** from **NVIDIA** Riva and other dependencies.

Run the setup script:

```bash
./scripts/build.sh
```

This script:

- downloads required pyhton modules

- downloads required client libraries

- prepares the text-to-speech environment

### 4️⃣ Set Environment Variables

Create a `.env` file in the root directory.

```js
NVIDIA_API_KEY=
GEMINI_API_KEY=
ALLOWED_ORIGINS=            (cors for deployment)
PYHTON_VERSION=             (optional)
```

These keys are required for:

- Chat generation via NVIDIA NIM

- Backup responses using Gemini 2.5 Flash Lite

### 5️⃣ Start the Server

for production:

```bash
fastapi run
```

for development:

```bash
fastapi dev
```

The API will start at:

```bash
http://localhost:8000
```

### 6️⃣ Access API Documentation

Open in browser:

```bash
http://localhost:8000/scalar_docs/
```

or

```bash
http://localhost:8000/docs/
```

This provides interactive API testing.
## 🤖 AI Models Used

### Primary Chat Model

**GPT OSS 120B**
Accessed via **NVIDIA NIM**.

Used for:

- main chat generation

- contextual conversation responses
---
### Backup Chat Model

**Gemini 2.5 Flash Lite**

Used when:

- primary model fails

- request limits are hit

- latency fallback is required
---
### Text-to-Speech

**Magpie Multilingual TTS**

Provided through **NVIDIA Riva**.

Used for:

- converting chatbot text responses into natural speech

- generating `.wav` audio for frontend playback

## 🚀 Tech Stack

Backend

- FastAPI

- Uvicorn

- Pydantic

- Python 3.11

AI Services

- NVIDIA NIM

- Gemini API

- Magpie TTS

Deployment

- Render

## 📡 API Endpoints

### 💬 Chat Response

Generates chatbot replies.

```bash
POST /api/v1/
```


**Request**

```json
[
  {
    "role": "user",
    "content": "Hello"
  }
]
```

**Response**

```json
{
  "role": "model",
  "content": "Hello! How can I support you today?",
  "model": "openai-oss-120b"
}
```

### 🧠 Conversation Title Generation

Automatically generates a title for a conversation thread.

```bash
POST /api/v1/convo/
```

Example use cases:

- chat history titles

- conversation summarization

### 🔊 Voice Generation

Converts text into realistic speech.

```bash
POST /api/v1/audio/
```

**Request**
```json
{
  "text": "Hello, I am MindMate.",
  "voice": "Aria"
}
```

**Response**

```bash
audio/wav
```

Generated using Magpie multilingual TTS.

### 🩺 Health Check

Used for API uptime monitoring and server pinging.

```bash
HEAD /health/
```

Returns:

```
200 OK
```

## 📚 API Documentation

Interactive documentation available at:

```bash
/scalar_docs/
/docs/
```

## 📂 Project Structure

```bash
mindmate-ai
├── ai
│   ├── __init__.py
│   └── ai.py
├── routes
│   ├── __init__.py
│   ├── deps.py
│   ├── convo_route.py
│   ├── msg_route.py
│   ├── audio_route.py
│   ├── scalar_docs.py
│   └── health.py
├── schemas
│   ├── __init__.py
│   ├── audio.py
│   └── msg.py
├── scripts
│   ├── build.sh
│   └── tts.sh
├── services
│   ├── __init__.py
│   ├── audio_response.py
│   └── response.py
├── main.py
├── README.md
├── LICENCE
└── requirements.txt
```

## 🧩 System Design Highlights

- LLM fallback architecture

- separate endpoints for chat, voice, and conversation metadata

- voice generation pipeline using NVIDIA TTS

- stateless API design for frontend integration

## ⚠ Disclaimer

MindMate AI is not a replacement for professional mental health services.
If you are experiencing a mental health crisis, please contact a qualified professional.

## 👨‍💻 Author

Built by **Srijan Kargupta**.

## 🏁 Hackathon Project

MindMate AI was developed as a hackathon project exploring:

- conversational AI

- AI-driven emotional support

- real-time neural speech synthesis
