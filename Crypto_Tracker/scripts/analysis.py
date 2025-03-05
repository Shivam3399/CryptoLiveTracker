import pandas as pd

EXCEL_FILE = "data/crypto_data.xlsx"

def analyze_crypto_data():
    """Performs analysis on cryptocurrency data from the Excel file."""
    try:
        # Load data from Excel
        df = pd.read_excel(EXCEL_FILE, engine='openpyxl')

        if df.empty:
            print("No data available in the Excel file.")
            return
        
        # 1️⃣ Find the top 5 cryptocurrencies by Market Cap
        top_5 = df.nlargest(5, "Market Cap")[["Name", "Market Cap"]]

        # 2️⃣ Calculate the average price of the top 50
        avg_price = df["Price (USD)"].mean()

        # 3️⃣ Identify the highest & lowest 24h % price change
        highest_change = df.loc[df["24h % Change"].idxmax(), ["Name", "24h % Change"]]
        lowest_change = df.loc[df["24h % Change"].idxmin(), ["Name", "24h % Change"]]

        # Print the results
        print("\n🔹 Top 5 Cryptocurrencies by Market Cap:")
        print(top_5.to_string(index=False))

        print(f"\n📊 Average Price of Top 50 Cryptocurrencies: ${avg_price:.2f}")

        print(f"\n📈 Highest 24h % Change: {highest_change['Name']} ({highest_change['24h % Change']:.2f}%)")
        print(f"📉 Lowest 24h % Change: {lowest_change['Name']} ({lowest_change['24h % Change']:.2f}%)")

    except Exception as e:
        print(f"Error analyzing data: {e}")

if __name__ == "__main__":
    analyze_crypto_data()
