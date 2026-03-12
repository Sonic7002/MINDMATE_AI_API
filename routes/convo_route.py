from fastapi import APIRouter, Depends, HTTPException
from msg import Msg, MsgRead
from response import generate_convo
from deps import get_convo_service

router = APIRouter(prefix="/convo",tags=["convo"])

@router.post("/", response_model=MsgRead)
def get_convo(data: list[Msg], service: generate_convo = Depends(get_convo_service)):
    try:
        return service(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
