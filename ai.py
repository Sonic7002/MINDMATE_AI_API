from msg import Msg, MsgRole, MsgRead
import requests
import os


def generate_response(prompt: str, msgs: list[Msg]) -> MsgRead:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    models = os.getenv("MODELS").split(',')

    data = [
        {
            "role": MsgRole.USER,
            "content": prompt
        }
    ]

    for msg in msgs:
        data.append(
            {
                "role": msg.role,
                "content": msg.content
            }
        )

    used_model = "not used"
    for model in models:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
                json={
                    "model": model,
                    "messages": data
                }
            )
            if response.status_code == 200:
                used_model = model
                try:
                    error = response.json()
                    print(error)
                    if error["error"]["code"] == 500:
                        continue
                except:
                    pass
                break
        except:
            continue

    if response.status_code == 200:
        try:
            reply = response.json()
            print (reply)
            return MsgRead(role=MsgRole.ASSISTANT, content=(reply["choices"][0]["message"]["content"]), model=used_model)
        except:
            raise ValueError("An error has occured please try again")
    else:
        raise ValueError("An error as occured try again")
