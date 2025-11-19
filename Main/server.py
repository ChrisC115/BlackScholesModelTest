from flask import Flask, jsonify
import alpaca_trade_api as tradeapi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = tradeapi.REST(
    "YOUR_KEY",          # Replace with your real API key
    "YOUR_SECRET",       # Replace with your real secret key
    "https://paper-api.alpaca.markets"
)

@app.route("/positions")
def get_positions():
    positions = api.list_positions()
    return jsonify([p._raw for p in positions])

@app.route("/account")
def get_account():
    account = api.get_account()
    return jsonify(account._raw)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
