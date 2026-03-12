from fastapi import APIRouter, Depends, HTTPException
from ..msg import Msg
from ..response import generate_convo
from ..deps import get_convo_service

router = APIRouter(prefix="/convo",tags=["convo"])

@router.get("/", response_model=Msg)
def get_convo(data: Msg, service: generate_convo = Depends(get_convo_service)):
    try:
        return service(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
