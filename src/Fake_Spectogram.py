import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Load fake audio (force 16 kHz for fair comparison)
audio, sr = librosa.load("fake_voice.wav", sr=16000)

print("Sampling rate:", sr)
print("Duration (sec):", len(audio) / sr)
print("Min value:", audio.min())
print("Max value:", audio.max())

# 2️⃣ Short-Time Fourier Transform (STFT)
stft = librosa.stft(
    audio,
    n_fft=1024,
    hop_length=256
)

# 3️⃣ Convert complex values to magnitude
magnitude = np.abs(stft)

# 4️⃣ Convert magnitude to log scale (decibels)
log_magnitude = librosa.amplitude_to_db(
    magnitude,
    ref=np.max
)

# 5️⃣ Plot spectrogram
plt.figure(figsize=(10, 4))

librosa.display.specshow(
    log_magnitude,
    sr=sr,
    hop_length=256,
    x_axis="time",
    y_axis="hz"
)

plt.colorbar(label="Energy (dB)")
plt.title("Fake Voice Spectrogram")
plt.tight_layout()
plt.show()
