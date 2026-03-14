from pydantic import BaseModel, field_validator, ValidationInfo


class Audio(BaseModel):
    text : str
    voice: str

    @field_validator("text", "voice")
    @classmethod
    def not_empty(cls, text: str, info: ValidationInfo):
        if not text.strip():
            raise ValueError(f"{info.field_name} must not be empty")
        return text
