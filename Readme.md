# Voice Deepfake Forensics

This project explores the forensic differences between real human speech and synthetic (deepfake/TTS) speech using time–frequency analysis.

## Motivation
Voice-based fraud and vishing attacks increasingly rely on AI-generated speech. This project focuses on understanding how deepfake audio differs from real speech at the signal level, rather than relying only on black-box ML models.

## What this project does
- Records real human speech
- Generates synthetic speech using TTS
- Converts audio into spectrograms using STFT
- Visually compares real vs fake speech patterns
- Analyzes artifacts such as over-smoothing, missing high frequencies, and unnatural consistency

## Techniques Used
- Sampling theory
- Short-Time Fourier Transform (STFT)
- Log-magnitude spectrograms
- Audio normalization
- Time–frequency forensic analysis

## Current Status
- Spectrogram generation complete
- Real vs fake visual comparison complete
- Mel spectrograms and ML-based classification planned

## Why this matters (Cybersecurity Context)
Attackers often use short, low-quality synthetic audio for social engineering. Understanding spectral artifacts helps design better detection systems and awareness tools.

## Next Steps
- Mel spectrogram extraction
- Window-based analysis
- Lightweight classifier for detection
