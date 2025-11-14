from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import json
import pandas as pd
from pathlib import Path


import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any, List

import pandas as pd
import requests



data_dir = Path(__file__).resolve().parents[1] / "data"
data_dir.mkdir(parents=True, exist_ok=True)
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
  'X-CMC_PRO_API_KEY': '',
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
    print(df.head())
    df.to_excel(xlsx_path, index=False)


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)