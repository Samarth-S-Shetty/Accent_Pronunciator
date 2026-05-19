from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os
import io
import eng_to_ipa as ipa  # 👈 new

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

ACCENT_VOICES = {
    "us": "21m00Tcm4TlvDq8ikWAM",
    "uk": "AZnzlk1XvdvUeBnXmlld",
    "india": "pNInz6obpgDQGcFmaJgB",
}

class PronounceRequest(BaseModel):
    text: str
    accent: str

class IpaRequest(BaseModel):  # 👈 new
    text: str

@app.post("/pronounce")
def pronounce(req: PronounceRequest):
    voice_id = ACCENT_VOICES.get(req.accent, ACCENT_VOICES["us"])
    audio_generator = client.text_to_speech.convert(
        voice_id=voice_id,
        text=req.text,
        model_id="eleven_multilingual_v2",
    )
    audio_bytes = io.BytesIO(b"".join(audio_generator))
    return StreamingResponse(audio_bytes, media_type="audio/mpeg")

@app.post("/ipa")                # 👈 new endpoint
def get_ipa(req: IpaRequest):
    result = ipa.convert(req.text)
    return { "ipa": result }