from dotenv import load_dotenv
load_dotenv()
from routes import convo_route, msg_route
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="MINDMATE AI API")

origins = os.getenv("ALLOWED_ORIGINS", "*")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(convo_route.router, prefix="/api/v1")
app.include_router(msg_route.router, prefix="/api/v1")