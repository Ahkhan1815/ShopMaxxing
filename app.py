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

@app.route("/cartMaxx", methods=["POST"])
def cartMaxx():
    defaultProd= [
    "Apple MacBook Air 13-inch (M3, 2024)",
    "Dell XPS 13 Plus",
    "Sony WH-1000XM5 Wireless Noise-Canceling Headphones",
    "Bose QuietComfort Ultra Headphones",
    "Nike Air Zoom Pegasus 41",
    "ASICS Gel-Kayano 31",
    "Samsung 65\" QLED 4K Smart TV",
    "LG C3 55\" OLED 4K TV",
    "Dell UltraSharp U2723QE 27\" 4K Monitor",
    "ASUS TUF Gaming VG27AQ 27\" Gaming Monitor",
    "JBL Charge 5 Portable Bluetooth Speaker",
    "Sonos One (Gen 2) Smart Speaker",
    "Breville Smart Oven Air Fryer",
    "Cuisinart 4-Slice Compact Toaster"
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