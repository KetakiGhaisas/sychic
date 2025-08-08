from flask import Flask, request, jsonify
import random

app = Flask(__name__)

mystic_responses = [
    "The stars have spoken. 🜏",
    "What you seek is hidden in the shadows.",
    "Your energy echoes that of an old soul...",
    "You already know the answer, don't you?",
    "Something big is coming — brace yourself.",
    "A betrayal awaits. 🕯",
    "Time bends in your favor, but not yet."
]

@app.route("/mcp", methods=["POST"])
def handle_puch_request():
    data = request.get_json()

    # User message
    user_prompt = data.get("prompt", "")
    user_id = data.get("user_id", "unknown")

    # Return a cryptic response
    response = {
        "response": random.choice(mystic_responses),
        "user_id": user_id
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000)
