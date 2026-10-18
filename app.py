from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AFSAR AI Backend Ready!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    return jsonify({"reply": "You said: " + message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
