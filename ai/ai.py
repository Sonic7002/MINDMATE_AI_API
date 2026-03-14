from schemas.msg import Msg, MsgRole, MsgRead
import requests
import os
from google import genai
from google.genai import types

client = genai.Client()


def generate_gemini(prompt: str, msgs: list[Msg]) -> MsgRead:
    try:
        data = [
            types.Content(
                role=MsgRole.USER,
                parts=[types.Part(text=f"INSTRUCTIONS:\n{prompt}")]
            )
        ]

        for msg in msgs:
            data.append(
                types.Content(
                    role=msg.role,
                    parts=[types.Part(text=msg.content)]
                )
            )

        response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=data)
        reply = MsgRead(role=MsgRole.MODEL, content=response.text, model="google/gemini2.5")
        print("used model: gemini 2.5")
        return reply
    except:
        raise ValueError("An error has occured")


def generate_response(prompt: str, msgs: list[Msg]) -> MsgRead:
    NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
    url = "https://integrate.api.nvidia.com/v1/chat/completions"

    headers = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json"
    }

    content = [
        {
            "role": "system",
            "content": prompt
        }
    ]

    for msg in msgs:
        if msg.role == MsgRole.MODEL:
            content.append(
                {
                    "role": "assistant",
                    "content": msg.content
                }
            )
        else:
            content.append(
                {
                    "role": msg.role,
                    "content": msg.content
                }
            )
    
    try:
        data = {
            "model": "openai/gpt-oss-120b",
            "messages": content
        }

        response = requests.post(url, headers=headers, json=data)
        content = response.json()
        reply = MsgRead(role=MsgRole.MODEL, content=content['choices'][0]['message']['content'], model="openai")
        print("used model: openai")
        return reply
    except:
        return generate_gemini(prompt, msgs)



