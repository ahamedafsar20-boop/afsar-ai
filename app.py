
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "AFSAR AI Backend Ready!"

@app.route("/chat", methods=["POST"])
def chat():
    raw_data = request.get_data(as_text=True) or ""

    try:
        data = json.loads(raw_data)
        if isinstance(data, dict):
            message = data.get("message", "")
        else:
            message = raw_data
    except (json.JSONDecodeError, ValueError):
        message = raw_data

    return jsonify({"reply": "You said: " + str(message)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
