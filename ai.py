from msg import Msg, MsgRole, MsgRead
import requests
import json
import os


def generate_response(prompt: str, msgs: list[Msg]) -> MsgRead:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    models = os.getenv("MODELS")

    data = [
        {
            "role": MsgRole.SYSTEM,
            "content": prompt
        }
    ]

    for msg in msgs:
        if msg.role == MsgRole.SYSTEM:
            raise ValueError("Invalid role, role must not be system")
        data.append(
            {
                "role": msg.role,
                "content": msg.content
            }
        )

    used_model: str
    for model in models:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
                data=json.dumps({
                    "model": model,
                    "messages": data
                })
            )
            if response.status_code == 200:
                used_model = model
                break
        except:
            continue

    if response.status_code == 200:
        reply = response.json()
        return MsgRead(role=MsgRole.ASSISTANT, content=(reply["choices"][0]["message"]["content"]), model=used_model)
    else:
        return MsgRead(role=MsgRole.ASSISTANT, content="An Error has occured please try again", model=used_model)
