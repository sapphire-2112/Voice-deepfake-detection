# 🔊 Voice Deepfake Forensics

This project investigates **forensic differences between real human speech and synthetic (deepfake / TTS) speech** using **signal-level time–frequency analysis**.

Instead of treating deepfake detection as a black-box machine learning problem, the project builds understanding **from first principles of digital signal processing and human auditory perception**.

---

## 🎯 Motivation

Voice-based fraud, vishing, and impersonation attacks increasingly rely on **AI-generated speech**.  
While synthetic voices often sound convincing to humans, they exhibit **statistical and perceptual inconsistencies** at the signal level.

This project focuses on **why** deepfake audio differs from real speech — not just **whether** a model can classify it.

---

## 🔬 What This Project Does

- Records **real human speech** at 16 kHz  
- Uses **synthetic / TTS speech** for comparison  
- Converts audio into **time–frequency representations**  
- Analyzes:
  - spectral smoothness  
  - temporal variability  
  - predictability across perceptual frequency bands  
- Extracts **forensic features** that expose deepfake artifacts  

---

## 🧠 Core Concepts & Techniques

- Digital audio sampling & sampling rate (16 kHz)  
- Short-Time Fourier Transform (STFT)  
- Log-magnitude spectrograms (dB scale)  
- **Mel spectrograms (perceptual frequency modeling)**  
- Statistical feature extraction:
  - Mean (spectral shape)  
  - Variance (temporal fluctuation)  
  - Entropy (predictability / smoothness)  

---

## 🔍 Key Forensic Insight

Synthetic speech is optimized for **human perception**, not **statistical authenticity**.

As a result, deepfake audio often shows:
- Over-smoothed temporal energy  
- Reduced high-frequency micro-variation  
- Lower entropy across Mel frequency bands  
- Unnaturally stable spectral patterns  

These artifacts are subtle to humans but **measurable using signal statistics**.

---

## 🔐 Cybersecurity Context

From a security perspective, voice deepfakes represent a **signal-level impersonation attack**.

Understanding spectral and temporal artifacts helps in:
- designing lightweight detection systems  
- building explainable detectors (not black-box only)  
- improving awareness of AI-based social engineering threats  

This project treats deepfake detection as **perceptual anomaly detection**.

---

## ⚙️ Feature Extraction Pipeline

1. Load audio at 16 kHz  
2. Compute STFT (windowed frequency analysis)  
3. Convert magnitude to log scale (dB)  
4. Apply Mel filterbanks (80 Mel bands)  
5. Extract per-band features:
   - Mean energy  
   - Variance over time  
   - Entropy of energy distribution  
6. Combine features into a single vector for detection  

---

## 🚧 Current Status

- ✅ Audio loading & preprocessing  
- ✅ STFT and log-magnitude spectrograms  
- ✅ Mel spectrogram extraction  
- ✅ Feature extraction:
  - Mean  
  - Variance  
  - Entropy  
- ✅ Reusable `extract_features()` pipeline  

---

## 🔮 Next Steps

- Numerical comparison of real vs fake feature vectors  
- Feature visualization (real vs fake curves)  
- Threshold-based detector  
- Lightweight ML classifier (Logistic Regression / SVM)  
- Window-based (1–3 sec) analysis for real-world attacks  

---

## 📌 Key Takeaway

> **Deepfake voices may sound real, but they fail to reproduce the natural variability and complexity of human speech.**  
> This project demonstrates how perceptual signal analysis exposes that gap.

---

## 🛠️ Tech Stack

- Python  
- Librosa  
- NumPy  
- Matplotlib  
- Digital Signal Processing (DSP)  

