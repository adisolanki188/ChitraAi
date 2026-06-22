from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

GEMINI_API_KEY = "YOUR_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate_page():
    return render_template("generate.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/generate-image", methods=["POST"])
def generate_image():

    data = request.json
    prompt = data.get("prompt")

    enhanced_prompt = f"""
    Generate a detailed image:
    {prompt}
    High quality, ultra realistic,
    4k, professional lighting
    """

    return jsonify({
        "status": "success",
        "prompt": enhanced_prompt,
        "message": "Connect Gemini Image Model API Here"
    })

if __name__ == "__main__":
    app.run(debug=True)
