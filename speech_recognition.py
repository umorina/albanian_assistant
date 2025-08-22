import openai
from config import OPENAI_API_KEY, LANGUAGE
import sounddevice as sd
import wave
import numpy as np

openai.api_key = OPENAI_API_KEY

def record_audio(filename="query.wav", duration=5, fs=16000):
    print("🎙️ Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wave.write(filename, fs, audio)

def transcribe(filename="query.wav"):
    with open(filename, "rb") as f:
        transcript = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=LANGUAGE
        )
    return transcript.text
