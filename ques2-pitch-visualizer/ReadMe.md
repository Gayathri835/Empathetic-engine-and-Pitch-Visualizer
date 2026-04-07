Pitch Visualizer is a Flask-based web app that converts a short story into a visual storyboard using AI-generated images.

Features
Text input (3–5 sentences)
Splits story into scenes
Enhances prompts for better visuals
Generates images using Stable Diffusion
Displays storyboard with captions
Supports styles (Digital, Realistic, Cartoon)

Tech Stack
Python, Flask
HTML (Jinja2)
Hugging Face API

Install dependencies:
pip install flask requests
Add your Hugging Face token in app.py:
HF_TOKEN = "hf_your_token_here"
Run:
python app.py
Open:
http://127.0.0.1:5000

Example
Input:
A business struggled with manual work. They adopted an AI tool. Now they save time and grow faste
