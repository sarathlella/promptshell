import sounddevice as sd
import numpy as np
import tempfile
import scipy.io.wavfile as wav

def record_audio(duration=5, sample_rate=48000, device=3):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16', device=device)
    sd.wait()
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_wav.name, sample_rate, audio)
    return temp_wav.name
