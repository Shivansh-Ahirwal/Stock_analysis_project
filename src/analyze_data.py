# src/analyze_data.py

import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from db_config import DB_PARAMS

# Connect to the PostgreSQL database
conn = psycopg2.connect(**DB_PARAMS)
df = pd.read_sql("SELECT * FROM stock_data ORDER BY datetime", conn)
conn.close()

# Calculate Simple Moving Averages (SMA)
df['SMA_20'] = df['close'].rolling(window=20).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()

# Plot the closing prices and SMAs
plt.figure(figsize=(14, 7))
plt.plot(df['datetime'], df['close'], label='Close Price')
plt.plot(df['datetime'], df['SMA_20'], label='20-Day SMA')
plt.plot(df['datetime'], df['SMA_50'], label='50-Day SMA')

# Strategy: Buy when SMA_20 crosses above SMA_50, Sell when SMA_20 crosses below SMA_50
df['Signal'] = 0
df['Signal'][df['SMA_20'] > df['SMA_50']] = 1
df['Signal'][df['SMA_20'] < df['SMA_50']] = -1

# Plot signals
plt.plot(df[df['Signal'] == 1]['datetime'], df[df['Signal'] == 1]['close'], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(df[df['Signal'] == -1]['datetime'], df[df['Signal'] == -1]['close'], 'v', markersize=10, color='r', label='Sell Signal')

plt.title('SMA Crossover Strategy')
plt.legend()
plt.show()
