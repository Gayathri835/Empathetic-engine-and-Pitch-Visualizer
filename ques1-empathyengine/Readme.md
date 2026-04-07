# Empathy Engine 

## Overview
The Empathy Engine is an AI-based system that converts text into emotionally expressive speech. 
It detects the sentiment and intensity of input text and dynamically adjusts vocal characteristics 
such as speech rate and volume to produce more human-like audio output.

---

## Features
- Emotion Detection (Positive, Negative, Neutral)
- Emotion Intensity Scaling (Bonus Feature)
- Dynamic Voice Modulation
- Audio Output Generation (.mp3)

---

## Tech Stack
- Python
- TextBlob (Sentiment Analysis)
- pyttsx3 (Text-to-Speech)

---

## Installation

pip install -r requirements.txt  
python -m textblob.download_corpora  

---

## Run the Application

python main.py  

---

## Example

Input:
"I am extremely happy today!"

Output:
- Emotion: Positive
- Faster speech rate
- Higher volume
- Generated expressive audio file

---

## Design Logic

### Emotion Detection
Uses TextBlob polarity:
- Positive → polarity > 0.2
- Negative → polarity < -0.2
- Neutral → otherwise

### Intensity Scaling
Intensity = absolute polarity  
Higher intensity → stronger voice modulation

### Voice Mapping

| Emotion  | Rate                | Volume              |
|----------|---------------------|---------------------|
| Positive | Faster              | Slightly louder     |
| Negative | Slower              | Softer              |
| Neutral  | Normal              | Normal              |

---

## Output
Audio file is saved as:
output.mp3
