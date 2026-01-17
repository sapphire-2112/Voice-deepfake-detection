import sounddevice as sd
from scipy.io.wavfile import write

duration = 2          # seconds
sample_rate = 16000   # important for speech

print("Recording...")
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32"
)
sd.wait()
print("Done recording")

write("my_voice.wav", sample_rate, audio)
