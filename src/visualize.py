import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests  
import json
from requests import Request, Session

# directories (same as original)
data_dir = Path(__file__).resolve().parents[1] / "datasets"
data_dir.mkdir(parents=True, exist_ok=True)

bda_path = data_dir / "BDA index.xlsx"
btc_path = data_dir / "btc price.xlsx"
fng_path = data_dir / "fng.xlsx"

results_dir = Path(__file__).resolve().parents[1] / "results"
results_dir.mkdir(parents=True, exist_ok=True)


def _load_series():
    fng = pd.read_excel(fng_path)
    bda = pd.read_excel(bda_path)
    btc = pd.read_excel(btc_path)

    # Fix column names
    fng = fng.rename(columns={"timestamp": "Date", "value": "FNG"})
    bda = bda.rename(
        columns={
            "Effective date ": "Date",
            "S&P Cryptocurrency Broad Digital Asset Index (USD)": "BDA",
        }
    )
    btc = btc.rename(columns={"timestamp": "Date", "value": "Bitcoin Price"})

    # Convert date
    fng["Date"] = pd.to_datetime(fng["Date"])
    bda["Date"] = pd.to_datetime(bda["Date"])
    btc["Date"] = pd.to_datetime(btc["Date"])

    # Sort by date
    fng = fng.sort_values("Date")
    bda = bda.sort_values("Date")
    btc = btc.sort_values("Date")

    return fng, bda, btc


# -------- simple individual plots --------

def plot_fng():
    fng, _, _ = _load_series()

    plt.figure(figsize=(6, 3))
    plt.plot(fng["Date"], fng["FNG"])
    plt.xlabel("Date")
    plt.ylabel("FNG")
    plt.title("Crypto Fear & Greed Index Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(results_dir / "Figure_1.png")
    plt.show()


def plot_bda():
    _, bda, _ = _load_series()

    plt.figure(figsize=(6, 3))
    plt.plot(bda["Date"], bda["BDA"])
    plt.xlabel("Date")
    plt.ylabel("BDA")
    plt.title("BDA Index Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(results_dir / "Figure_2.png")
    plt.show()


def plot_btc():
    _, _, btc = _load_series()

    plt.figure(figsize=(6, 3))
    plt.plot(btc["Date"], btc["Bitcoin Price"])
    plt.xlabel("Date")
    plt.ylabel("Bitcoin Price")
    plt.title("Bitcoin Price Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(results_dir / "Figure_3.png")
    plt.show()


# -------- combined dual-axis plots --------

def plot_fng_bda():
    fng, bda, _ = _load_series()

    merged = pd.merge(fng, bda, on="Date", how="inner")

    start = pd.to_datetime("2024-05-02")
    end = pd.to_datetime("2025-11-06")
    mask = (merged["Date"] >= start) & (merged["Date"] <= end)
    plot_df = merged.loc[mask].copy()

    fig, ax1 = plt.subplots(figsize=(8, 4))

    line1 = ax1.plot(plot_df["Date"], plot_df["BDA"], label="BDA Index")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("BDA Index")
    ax1.tick_params(axis="y")

    ax2 = ax1.twinx()
    line2 = ax2.plot(
        plot_df["Date"],
        plot_df["FNG"],
        color="orange",
        label="Fear & Greed Index",
    )
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


def plot_fng_btc():
    fng, _, btc = _load_series()

    merged = pd.merge(fng, btc, on="Date", how="inner")

    start = pd.to_datetime("2024-05-02")
    end = pd.to_datetime("2025-11-06")
    mask = (merged["Date"] >= start) & (merged["Date"] <= end)
    plot_df = merged.loc[mask].copy()

    fig, ax1 = plt.subplots(figsize=(8, 4))

    line1 = ax1.plot(plot_df["Date"], plot_df["Bitcoin Price"], label="Bitcoin Price")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Bitcoin Price")
    ax1.tick_params(axis="y")

    ax2 = ax1.twinx()
    line2 = ax2.plot(
        plot_df["Date"],
        plot_df["FNG"],
        color="orange",
        label="Fear & Greed Index",
    )
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


def plot_bda_btc():
    _, bda, btc = _load_series()

    merged = pd.merge(btc, bda, on="Date", how="inner")

    start = pd.to_datetime("2024-05-02")
    end = pd.to_datetime("2025-11-06")
    mask = (merged["Date"] >= start) & (merged["Date"] <= end)
    plot_df = merged.loc[mask].copy()

    fig, ax1 = plt.subplots(figsize=(8, 4))

    line1 = ax1.plot(plot_df["Date"], plot_df["Bitcoin Price"], label="Bitcoin Price")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Bitcoin Price")
    ax1.tick_params(axis="y")

    ax2 = ax1.twinx()
    line2 = ax2.plot(
        plot_df["Date"],
        plot_df["BDA"],
        color="orange",
        label="BDA Index",
    )
    ax2.set_ylabel("BDA Index")
    ax2.tick_params(axis="y")

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper left")

    fig.suptitle("BDA Index vs Bitcoin Price")
    fig.tight_layout()
    plt.savefig(results_dir / "Figure_6.png")
    plt.show()


def run_all_plots():   
    plot_fng()
    plot_bda()
    plot_btc()
    plot_fng_bda()
    plot_fng_btc()
    plot_bda_btc()





