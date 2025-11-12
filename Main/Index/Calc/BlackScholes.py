from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

# Initialize the trading client for paper trading
trading_client = TradingClient(
    api_key="PKFCNT5XIAUJTKGKBBMQCHRAHE",
    secret_key="7oohUukYy6ACFc4YVywTZiY34NhsGKtu5DxYsacghLus",
    paper=True  # This makes sure it connects to paper-api.alpaca.markets
)

# Get account information
account = trading_client.get_account()

# Check if your account is restricted
if account.trading_blocked:
    print("Account is currently restricted from trading.")
else:
    print("Trading is active.")

# Show available buying power
print(f"${account.buying_power} is available as buying power.")
