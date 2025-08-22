from gtts import gTTS
import os
from config import LANGUAGE

def speak(text):
    print("🔊 Speaking:", text)
    tts = gTTS(text=text, lang=LANGUAGE)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")
