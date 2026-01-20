import numpy as np
from MEL_Spectrogram import log_MEL_Spectro
def extract_features(audio,sr,n_mels=80): 
    mel_spec=librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mels)
    log_MEL_Spectro=librosa.power_to_db(mel_spec, ref=np.max)
    Mean=np.mean(log_MEL_Spectro, axis=1)
    Varience=np.var(log_MEL_Spectro, axis=1)
    pos_val=np.exp(log_MEL_Spectro)
    prob=pos_val/np.sum(pos_val, axis=1,keepdims=True)
    entropy = -np.sum(prob * np.log(prob + 1e-10), axis=1)
## sr is sampling rate it is the measurements taken per second which is fixed and 16000 here.

    combine_features=np.concatenate((Mean, Varience, entropy), axis=0)
    return combine_features