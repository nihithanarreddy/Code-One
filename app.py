from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("API_KEY")

# ---------- ROUTES ----------

@app.route('/')
def home():
    return "Flask backend is running successfully"

@app.route("/explain_code", methods=["POST"])
def explain_code():
    try:
        data = request.get_json()
        code = data.get("code", "")
        mode = data.get("mode", "simple")

        prompt = f"Explain this code in {mode} mode:\n\n{code}"

        # ✅ Updated OpenAI API call
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        explanation = response.choices[0].message.content
        return jsonify({"explanation": explanation})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/data', methods=["GET"])
def get_data():
    return jsonify({"data": "This is data from Flask backend!"})

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
