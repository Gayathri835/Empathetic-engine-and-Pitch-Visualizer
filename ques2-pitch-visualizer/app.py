from flask import Flask, render_template, request
import requests
import uuid
import os

app = Flask(__name__)
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}
# -------- Split Story --------
def split_story(text):
    sentences = text.split(".")
    return [s.strip() for s in sentences if s.strip()][:3]

# -------- Enhance Prompt --------
def enhance_prompt(sentence, style):
    return f"{sentence}, cinematic lighting, highly detailed, {style}, storytelling illustration, 4k"

# -------- Generate Image --------
def generate_image(prompt):
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    # Handle errors
    if response.status_code != 200:
        print("API Error:", response.text)
        return None

    img_data = response.content

    os.makedirs("static", exist_ok=True)

    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join("static", filename)

    with open(filepath, "wb") as f:
        f.write(img_data)

    return f"/static/{filename}"  

# -------- Route --------
@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    captions = []

    if request.method == "POST":
        text = request.form.get("story")
        style = request.form.get("style", "digital art")

        if text:
            sentences = split_story(text)

            for sentence in sentences:
                prompt = enhance_prompt(sentence, style)
                img_path = generate_image(prompt)

                if img_path:
                    images.append(img_path)
                    captions.append(sentence)

    return render_template("index.html", images=images, captions=captions)


# -------- Run --------
if __name__ == "__main__":
    app.run(debug=True)
