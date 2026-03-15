from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="MINDMATE AI API")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not GEMINI_API_KEY or not NVIDIA_API_KEY:
    raise RuntimeError("Fatal Eror! one or more API keys are missing.")

origins = os.getenv("ALLOWED_ORIGINS", "*")

if origins == "*":
    origins = ["*"]
else:
    origins = origins.split(",")

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

from routes import convo_route, msg_route, health, scalar_docs, audio_route
app.include_router(convo_route.router, prefix="/api/v1")
app.include_router(msg_route.router, prefix="/api/v1")
app.include_router(audio_route.router, prefix="/api/v1")
app.include_router(health.router)
app.include_router(scalar_docs.router)