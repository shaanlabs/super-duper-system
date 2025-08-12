from flask import Flask, render_template, request, jsonify
from ollama_client import ask_ollama

app = Flask(__name__)

MODEL_NAME = "gpt-oss:20b"  # Change model here

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_prompt = request.json.get("prompt")
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    reply = ask_ollama(MODEL_NAME, user_prompt)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
