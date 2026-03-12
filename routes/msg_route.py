from fastapi import APIRouter, Depends, HTTPException
from msg import Msg, MsgRead
from response import generate_msg
from deps import get_msg_service

router = APIRouter(tags=["msgs"])

@router.post("/", response_model=MsgRead)
def get_reply(data: list[Msg], service: generate_msg = Depends(get_msg_service)):
    try:
        return service(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
