import subprocess
from uuid import uuid4
import os
from schemas.audio import Audio
from fastapi import UploadFile
import tempfile

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
        
    def generate_text(self, file: UploadFile) -> str:
        tmp_path = None

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(file.file.read())
                tmp_path = tmp.name

            result = subprocess.run(
                ["./scripts/stt.sh", tmp_path],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                raise ValueError(result.stderr)

            output = result.stdout

            transcript = None
            for line in output.splitlines():
                if "Final transcript:" in line:
                    transcript = line.split("Final transcript:")[1].strip()

            if not transcript:
                raise ValueError("Transcript not found")

            return  transcript
        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)

    def cleanup(self, output_file: str):
            if os.path.exists(output_file):
                os.remove(output_file)
            else:
                raise ValueError("file does not exist")