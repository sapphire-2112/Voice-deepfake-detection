from gtts import gTTS

text = "Hello, this is a synthetic voice generated for testing deepfake detection."
tts = gTTS(text=text, lang="en")
tts.save("fake_voice.mp3")
