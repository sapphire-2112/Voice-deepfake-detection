import librosa
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Data")
audio, sr = librosa.load(
    os.path.join(DATA_DIR, "my_voice.wav"),
    sr=16000
)

print("Sampling rate:", sr)
print("Duration (sec):", len(audio) / sr)
print("Min value:", audio.min())
print("Max value:", audio.max())
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 3))
plt.plot(audio)
plt.title("Waveform (Time Domain)")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

