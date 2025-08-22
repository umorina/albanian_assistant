import pvporcupine
import pyaudio, struct

def listen_for_wake_word():
    porcupine = pvporcupine.create(keywords=["hej Jola"])  # placeholder, later "Hej Ora"
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1,
                     rate=porcupine.sample_rate, input=True,
                     frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        result = porcupine.process(pcm)
        if result >= 0:
            return True
