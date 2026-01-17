import librosa

audio, sr = librosa.load("my_voice.wav", sr=None)

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

