from services.response import generate_convo, generate_msg
from services.audio_response import AudioService

def get_msg_service() -> generate_msg:
    return generate_msg

def get_convo_service() -> generate_convo:
    return generate_convo

def get_audio_service() -> AudioService:
    return AudioService()