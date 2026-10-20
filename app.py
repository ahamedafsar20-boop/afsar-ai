
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "AFSAR AI Backend Ready!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        raw_data = request.get_data(as_text=True)
        data = json.loads(raw_data) if raw_data else {}
        message = data.get("message", "")
        return jsonify({"reply": "You said: " + str(message)})
    except Exception:
        return jsonify({"reply": "Message received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
