import pyttsx3
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
# Initialize
engine = pyttsx3.init()
sia = SentimentIntensityAnalyzer()
# -------- Emotion Detection --------
def detect_emotion(text: str):
    """Return emotion category and intensity using VADER sentiment analysis."""
    scores = sia.polarity_scores(text)
    polarity = scores['compound']  # (-1 to +1)
    intensity = abs(polarity)

    if polarity > 0.2:
        emotion = "positive"
    elif polarity < -0.2:
        emotion = "negative"
    else:
        emotion = "neutral"

    return emotion, intensity
# -------- Voice Settings --------
def apply_voice_settings(emotion: str, intensity: float):
    """Adjust speech rate and volume depending on emotion."""
    
    # Default values
    rate = 150
    volume = 0.9

    if emotion == "positive":
        rate = 170 + int(30 * intensity)
        volume = 0.9 + (0.1 * intensity)

    elif emotion == "negative":
        rate = 140 - int(30 * intensity)
        volume = 0.8 - (0.2 * intensity)

    # Clamp volume between 0 and 1
    volume = max(0.0, min(volume, 1.0))

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    return rate, volume
# -------- Speak Function --------
def speak(text: str, emotion: str, intensity: float):
    """Speak text aloud and save audio file."""

    rate, volume = apply_voice_settings(emotion, intensity)

    print(f"\nEmotion: {emotion} | Intensity: {round(intensity, 2)}")
    print(f"Rate: {rate}, Volume: {round(volume, 2)}")

    # Speak
    engine.say(text)

    # Save audio (NOTE: mp3 may not work on all systems → use .wav if issue)
    engine.save_to_file(text, "output.wav")

    engine.runAndWait()

    print("Audio saved as output.wav")
# -------- MAIN --------
if __name__ == "__main__":
    print("=== Empathy Engine (VADER Edition) ===")
    user_text = input("Enter your text: ")

    emotion, intensity = detect_emotion(user_text)
    speak(user_text, emotion, intensity)
