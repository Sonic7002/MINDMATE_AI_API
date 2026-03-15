from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, UploadFile, File
from schemas.audio import Audio
from fastapi.responses import FileResponse
from services.audio_response import AudioService
from .deps import get_audio_service

router = APIRouter(prefix="/audio",tags=["audio"])


@router.post("/")
def get_audio(data: Audio, background_tasks: BackgroundTasks, service: AudioService = Depends(get_audio_service)) -> FileResponse:
    try:
        output_file = service.generate_audio(data)
        response = FileResponse(output_file, media_type="audio/wav", filename="tts_output.wav")

        background_tasks.add_task(service.cleanup, output_file)

        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/text")
def get_text(file: UploadFile = File(...), service: AudioService = Depends(get_audio_service)):
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="Only .wav files allowed")
    try:
        text = service.generate_text(file)
        return {"transcript": text}
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
