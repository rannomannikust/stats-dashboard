import requests
import pandas as pd

def get_pa103_data(indicator="GR_W_AVG", emtak="TOTAL"):
    url = "https://andmed.stat.ee/api/v1/et/stat/PA103"
    payload = {
        "query": [
            {"code": "Näitaja", "selection": {"filter": "item", "values": [indicator]}},
            {"code": "Tegevusala", "selection": {"filter": "item", "values": [emtak]}}
            # Vaatlusperioodi ei piira → tagastab kõik aastad
        ],
        "response": {"format": "json"}
    }
    res = requests.post(url, json=payload)
    res.raise_for_status()
    data = res.json()
    rows = data['data']
    return pd.DataFrame([{
        "näitaja": row['key'][0],
        "tegevusala": row['key'][1],
        "aasta": row['key'][2],
        "väärtus": float(row['values'][0]) if row['values'][0] else None
    } for row in rows])
