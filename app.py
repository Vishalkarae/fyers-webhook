from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  # We'll set this later on Render

@app.route('/fyers', methods=['POST'])
def fyers_webhook():
    data = request.json
    action = data.get("action")  # BUY or SELL

    order = {
        "symbol": "NSE:RELIANCE-EQ",  # Change as per your needs
        "qty": 1,
        "type": 2,
        "side": 1 if action == "BUY" else -1,
        "productType": "INTRADAY",
        "limitPrice": 0,
        "stopPrice": 0,
        "validity": "DAY",
        "disclosedQty": 0,
        "offlineOrder": False,
        "stopLoss": 0,
        "takeProfit": 0
    }

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.post("https://api.fyers.in/api/v2/orders", json=order, headers=headers)

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
