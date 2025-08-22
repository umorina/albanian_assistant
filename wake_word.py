import pvporcupine
import pyaudio
import struct
from config import PICOVOICE_ACCESS_KEY, WAKEWORD_FILE

class WakeWordDetector:
    def __init__(self):
        self.porcupine = pvporcupine.create(
            access_key=PICOVOICE_ACCESS_KEY,
            keyword_paths=[WAKEWORD_FILE]
        )
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def listen(self):
        pcm = self.audio_stream.read(self.porcupine.frame_length, exception_on_overflow=False)
        pcm_unpacked = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
        keyword_index = self.porcupine.process(pcm_unpacked)
        return keyword_index >= 0

    def close(self):
        self.audio_stream.close()
        self.pa.terminate()
        self.porcupine.delete()
