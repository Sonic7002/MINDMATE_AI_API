from fastapi import APIRouter, Depends, HTTPException
from ..msg import Msg
from ..response import generate_msg
from ..deps import get_msg_service

router = APIRouter(tags=["msgs"])

@router.get("/", response_model=Msg)
def get_reply(data: list[Msg], service: generate_msg = Depends(get_msg_service)):
    try:
        return service(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
