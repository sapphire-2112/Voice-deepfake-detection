import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import Converting_into_numbers as cin
stft=librosa.stft(cin.audio,n_fft=1024,hop_length=256)
magnitude=np.abs(stft)
log_magnitude=librosa.amplitude_to_db(magnitude,ref=np.max)
plt.figure(figsize=(10, 4))
librosa.display.specshow(log_magnitude, sr=cin.sr, hop_length=256, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Log-Magnitude Spectrogram')
plt.tight_layout()
plt.show()