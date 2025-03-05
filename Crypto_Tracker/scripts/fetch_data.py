import requests
import pandas as pd

# API URL for fetching the top 50 cryptocurrencies from CoinGecko
API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_crypto_data():
    """Fetches live cryptocurrency data for the top 50 by market capitalization."""
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,  # Get the top 50
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an error for failed requests
        data = response.json()

        # Extract relevant fields
        crypto_list = []
        for coin in data:
            crypto_list.append({
                "Name": coin["name"],
                "Symbol": coin["symbol"].upper(),
                "Price (USD)": coin["current_price"],
                "Market Cap": coin["market_cap"],
                "24h Volume": coin["total_volume"],
                "24h % Change": coin["price_change_percentage_24h"]
            })

        # Convert to DataFrame
        df = pd.DataFrame(crypto_list)
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    df = fetch_crypto_data()
    if df is not None:
        print(df.head())  # Display first few rows
