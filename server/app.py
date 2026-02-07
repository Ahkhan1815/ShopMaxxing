import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/cartMaxx")
def cartMaxx():
    defaultProd= [
    "Apple MacBook Air 13-inch (M3)",
    "Dell XPS 13",
    "Sony WH-1000XM5",
    "Bose QuietComfort Ultra Headphones",
    "Nike Air Zoom Pegasus 41",
    "ASICS Gel-Kayano 31",
    "Instant Pot Duo 7-in-1 (6 Qt)",
    "Ninja AF101 Air Fryer (4 Qt)"
    ]
    
    defaultPref = {
    "laptpps": [
      "Lightweight",
      "Under $1400",
      "Good battery life"
    ],
    "HEADPHONES": [
      "Strong noise cancelation",
      "Comfortable for long sessions",
      "Wireless"
    ],
    "running shose": [
      "Good for overpronation",
      "Comfortable for daily runs",
      "Durable outsole"
    ],
    "tv & home theater": [
      "At least 55 inches",
      "Good for movies",
      "Good contrast in dark scenes"
    ]
    }

    data = request.get_json()
    productName = data.get("productName", defaultProd)
    preferences = data.get("preferences", defaultPref)
    response = client.responses.create(
    prompt={
        "id": "pmpt_69878f57c9448194abf8fc9a3d3fe45906ae572b4de76c34",
        "version": "3",
        "variables": {
        "productnames": json.dumps(productName),
        "preferences": json.dumps(preferences)
        }
    }
    )

    text = response.output[0].content[0].text
    return text

@app.route("/")
def test():
    return "test"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=4000)