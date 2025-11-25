import os
import requests
import json
import pandas as pd
import numpy as np
from pathlib import Path
from requests import Request, Session
import matplotlib.pyplot as plt

data_dir = Path(__file__).resolve().parents[1] / "data2"
data_dir.mkdir(parents=True, exist_ok=True)
bda_path = data_dir / "BDA index.xlsx"
btc_path = data_dir / "btc price.xlsx"
fng_path = data_dir / "fng.xlsx"

results_dir = Path(__file__).resolve().parents[1] / "results"
results_dir.mkdir(exist_ok=True)

fng = pd.read_excel(fng_path)
bda = pd.read_excel(bda_path)
btc = pd.read_excel(btc_path)

# Fix column names
fng = fng.rename(columns={'timestamp':'Date','value':'FNG'})
bda = bda.rename(columns={'Effective date ':'Date',
                          'S&P Cryptocurrency Broad Digital Asset Index (USD)':'BDA'})
btc = btc.rename(columns={'timestamp':'Date','value':'Bitcoin Price'})

# Convert date
fng['Date'] = pd.to_datetime(fng['Date'])
bda['Date'] = pd.to_datetime(bda['Date'])
btc['Date'] = pd.to_datetime(btc['Date'])

# Sort by date
fng = fng.sort_values('Date')
bda = bda.sort_values('Date')
btc = btc.sort_values('Date')

# --- Plot FNG ---
plt.figure(figsize=(10,5))
plt.plot(fng['Date'], fng['FNG'])
plt.xlabel("Date")
plt.ylabel("FNG")
plt.title("Crypto Fear & Greed Index Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(results_dir / "Figure_1.png")
plt.show()

# --- Plot BDA ---
plt.figure(figsize=(10,5))
plt.plot(bda['Date'], bda['BDA'])
plt.xlabel("Date")
plt.ylabel("BDA")
plt.title("BDA Index Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(results_dir / "Figure_2.png")
plt.show()

# --- Plot BTC ---
plt.figure(figsize=(10,5))
plt.plot(btc['Date'], btc['Bitcoin Price'])
plt.xlabel("Date")
plt.ylabel("Bitcoin Price")
plt.title("Bitcoin Price Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(results_dir / "Figure_3.png")
plt.show()

# --- Plot FNG and BDA ---
merged = pd.merge(fng, bda, on="Date", how="inner")

start = pd.to_datetime("2024-05-02")
end   = pd.to_datetime("2025-11-06")
mask = (merged["Date"] >= start) & (merged["Date"] <= end)
plot_df = merged.loc[mask].copy()

fig, ax1 = plt.subplots(figsize=(12, 6))

line1 = ax1.plot(plot_df["Date"], plot_df["BDA"], label="BDA Index")
ax1.set_xlabel("Date")
ax1.set_ylabel("BDA Index")
ax1.tick_params(axis="y")

ax2 = ax1.twinx()
line2 = ax2.plot(plot_df["Date"], plot_df["FNG"], color="orange", label="Fear & Greed Index")
ax2.set_ylabel("Fear & Greed Index")
ax2.set_ylim(0, 100)   
ax2.tick_params(axis="y")

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

fig.suptitle("Fear & Greed Index vs BDA Index")
fig.tight_layout()
plt.savefig(results_dir / "Figure_4.png")
plt.show()

# --- Plot FNG and BTC ---
merged = pd.merge(fng, btc, on="Date", how="inner")

start = pd.to_datetime("2024-05-02")
end   = pd.to_datetime("2025-11-06")
mask = (merged["Date"] >= start) & (merged["Date"] <= end)
plot_df = merged.loc[mask].copy()

fig, ax1 = plt.subplots(figsize=(12, 6))

line1 = ax1.plot(plot_df["Date"], plot_df["Bitcoin Price"], label="Bitcoin Price")
ax1.set_xlabel("Date")
ax1.set_ylabel("Bitcoin Price")
ax1.tick_params(axis="y")

ax2 = ax1.twinx()
line2 = ax2.plot(plot_df["Date"], plot_df["FNG"], color="orange", label="Fear & Greed Index")
ax2.set_ylabel("Fear & Greed Index")
ax2.set_ylim(0, 100)   
ax2.tick_params(axis="y")

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

fig.suptitle("Fear & Greed Index vs Bitcoin Price")
fig.tight_layout()
plt.savefig(results_dir / "Figure_5.png")
plt.show()

# --- Plot BDA and BTC ---
merged = pd.merge(btc, bda, on="Date", how="inner")

start = pd.to_datetime("2024-05-02")
end   = pd.to_datetime("2025-11-06")
mask = (merged["Date"] >= start) & (merged["Date"] <= end)
plot_df = merged.loc[mask].copy()

fig, ax1 = plt.subplots(figsize=(12, 6))

line1 = ax1.plot(plot_df["Date"], plot_df["Bitcoin Price"], label="Bitcoin Price")
ax1.set_xlabel("Date")
ax1.set_ylabel("Bitcoin Price")
ax1.tick_params(axis="y")

ax2 = ax1.twinx()
line2 = ax2.plot(plot_df["Date"], plot_df["BDA"], color="orange", label="BDA Index")
ax2.set_ylabel("BDA Index") 
ax2.tick_params(axis="y")

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

fig.suptitle("BDA Index vs Bitcoin Price")
fig.tight_layout()
plt.savefig(results_dir / "Figure_6.png")
plt.show()




