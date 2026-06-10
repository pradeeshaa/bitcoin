import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download Bitcoin data
btc = yf.download(
    "BTC-USD",
    start="2020-01-01",
    end="2025-01-01"
)

# Show first rows
print(btc.head())

# Save to CSV
btc.to_csv("bitcoin_data.csv")

# Plot Bitcoin closing price
plt.figure(figsize=(10,5))
plt.plot(btc.index, btc['Close'])

plt.title("Bitcoin Closing Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)

plt.show()