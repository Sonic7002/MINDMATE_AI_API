from enum import Enum
from pydantic import BaseModel, field_validator, ValidationInfo

class MsgRole(str, Enum):
    ASSISTANT = "assistant"
    USER = "user"
    SYSTEM = "system"

class Msg(BaseModel):
    role = MsgRole
    content: str

    @field_validator("content")
    @classmethod
    def not_empty(cls, text: str, info: ValidationInfo):
        if not text.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return text