import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import Converting_into_numbers as cin

Mel_Spectro=librosa.feature.melspectrogram(y=cin.audio, sr=cin.sr, n_mels=80)
log_MEL_Spectro=librosa.power_to_db(Mel_Spectro, ref=np.max)
fig=plt.figure(figsize=(10, 4))
librosa.display.specshow(log_MEL_Spectro, sr=cin.sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram (dB)')
plt.tight_layout()
plt.show()