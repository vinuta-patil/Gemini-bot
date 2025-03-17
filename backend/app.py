from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS  # ✅ Import CORS

# Explicitly load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"

# Debugging: Print API Key (ensure it's loaded correctly)
print("Loaded API Key:", API_KEY)

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    # Debugging: Print user input
    print("User Input:", user_input)

    headers = {"Content-Type": "application/json"}

    # ✅ Corrected JSON payload format
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ]
    }

    # Debugging: Print payload before sending request
    print("Payload being sent:", payload)

    response = requests.post(f"{GEMINI_URL}?key={API_KEY}", json=payload, headers=headers)

    # Debugging: Print response status and content
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)

    if response.status_code == 200:
        reply = response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")
        return jsonify({"response": reply})
    else:
        return jsonify({"error": f"Failed to fetch response: {response.text}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
