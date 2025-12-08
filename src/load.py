import os
import requests
import json
import pandas as pd
from pathlib import Path
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from datetime import datetime, timedelta, timezone
from typing import Dict, Any, List
from config import api_key

data_dir = Path(__file__).resolve().parents[1] / "data"
data_dir.mkdir(parents=True, exist_ok=True)

def get_fng_data1():
    
    #retrieve first 500 rows of fear and greed index data (since API query limit is 500)
    json_path = data_dir / "fng1.json"
    xlsx_path = data_dir / "fng1.xlsx"

    url = 'https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical'
    parameters = {
    'limit': 500 
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        rows = data.get("data", [])
        filtered = [
            {"timestamp": item.get("timestamp"), "value": item.get("value")}
            for item in rows
        ]

        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(filtered, jf, ensure_ascii=False, indent=2)
    
        df = pd.DataFrame(filtered, columns=["timestamp", "value"])
        df["Date"] = pd.to_datetime(df["timestamp"], unit='s')
        df = df.drop(columns=["timestamp"])
        df = df[["Date", "value"]]

        print(df.head())
        df.to_excel(xlsx_path, index=False)       

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def get_fng_data2():

    #retrieve remaining 60 rows of fear and greed index data 
    json_path = data_dir / "fng2.json"
    xlsx_path = data_dir / "fng2.xlsx"

    url = 'https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical'
    parameters = {
    'start':501,
    'limit': 60
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        rows = data.get("data", [])
        filtered = [
            {"timestamp": item.get("timestamp"), "value": item.get("value")}
            for item in rows
        ]

        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(filtered, jf, ensure_ascii=False, indent=2)
    
        df = pd.DataFrame(filtered, columns=["timestamp", "value"])
        df["Date"] = pd.to_datetime(df["timestamp"], unit='s')
        df = df.drop(columns=["timestamp"])
        df = df[["Date", "value"]]
        print(df.head())
        df.to_excel(xlsx_path, index=False)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)



def get_bitcoin_price_data():

    json_path = data_dir / "btc price.json"
    xlsx_path = data_dir / "btc price.xlsx"

    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/ohlcv/historical'
    parameters = {
    'id': 1,
    'count': 561,
    'interval': 'daily'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        rows = data.get("data").get('quotes')
        filtered = [
            {"timestamp": item['quote']['USD'].get("timestamp")[:10], "value": round(item['quote']['USD'].get("close"), 2)}
            for item in rows
        ]

        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(filtered, jf, ensure_ascii=False, indent=2)
    
        df = pd.DataFrame(filtered, columns=["timestamp", "value"])
        df.to_excel(xlsx_path, index=False)
        return df


    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    

