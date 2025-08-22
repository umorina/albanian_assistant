from wake_word import WakeWordDetector
from speech_recognition import record_audio, transcribe
from intent_parser import handle_intent
from tts import speak

def main():
    detector = WakeWordDetector()
    print("👂 Listening for 'Hej Ora'...")

    try:
        while True:
            if detector.listen():
                print("✅ Wake word detected!")
                record_audio("query.wav", duration=5)
                query = transcribe("query.wav")
                print("👂 Heard:", query)
                response = handle_intent(query)
                speak(response)
    except KeyboardInterrupt:
        print("👋 Exiting...")
    finally:
        detector.close()

if __name__ == "__main__":
    main()
