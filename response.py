from msg import Msg, MsgRead, MsgRole
from ai import generate_response

def generate_msg(msgs: list[Msg]) -> MsgRead:
    
    prompt = """You are a mental health support assistant.

    Rules:
    - You are NOT a therapist or medical professional.
    - You do NOT prescribe.
    - You provide emotional support, grounding, and coping suggestions.
    - If user expresses self-harm or suicidal intent:
    - Respond with empathy
    - Encourage seeking professional help
    - Suggest contacting local helplines
    - Do NOT provide instructions or validation for self-harm

    Tone:
    - Calm
    - Supportive
    - Non-judgmental
    - Clear and grounded

    Always prioritize user safety.
    """

    return generate_response(prompt, msgs)

def generate_convo(msg: Msg) -> MsgRead:
    if msg.role == MsgRole.USER:
        prompt = """You are generating a title for a chat conversation.

        Given the first message of the conversation, generate a short, clear, descriptive title.

        Rules:
        - Maximum 4 words
        - No punctuation at the end
        - No quotes
        - No emojis
        - No extra commentary
        - Output ONLY the title
        """

        return generate_response(prompt, msg)
    else:
        raise ValueError("Invalid role must be user")
