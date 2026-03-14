import subprocess
from uuid import uuid4
import os
from schemas.audio import Audio

class AudioService:
    def generate_audio(self, data: Audio) -> str:
        try:
            output_file = f"{uuid4()}.wav"
            subprocess.run(["./scripts/tts.sh", data.text, data.voice, output_file], check=True)
            
            if not os.path.exists(output_file):
                raise ValueError("Failed to generate audio, try again")
            
            return output_file
        except:
            raise ValueError("Failed to generate audio, try again")
        
    def cleanup(self, output_file: str):
            if os.path.exists(output_file):
                os.remove(output_file)
            else:
                raise ValueError("file does not exist")