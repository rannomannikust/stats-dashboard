import requests
import pandas as pd

def get_salary_data(year="2023", county="00", activity="TOTAL"):
    #url = "https://andmed.stat.ee/api/v1/et/majandus/RAA0012"
    #url =  "https://andmed.stat.ee/api/v1/et/majandus/palk-ja-toojeukulu/palk/aastastatistika/PA103.px"
    url =  "https://andmed.stat.ee/api/v1/et/stat/PA103"
    payload = {
        "query": [
            {"code": "Aasta", "selection": {"filter": "item", "values": [year]}},
            {"code": "Maakond", "selection": {"filter": "item", "values": [county]}},
            {"code": "Tegevusala", "selection": {"filter": "item", "values": [activity]}}
        ],
        "response": {"format": "json"}
    }

    res = requests.post(url, json=payload)
    res.raise_for_status()
    data = res.json()

    rows = data['data']
    df = pd.DataFrame([{
        "aasta": row['key'][0],
        "maakond": row['key'][1],
        "tegevusala": row['key'][2],
        "palk": row['values'][0]
    } for row in rows])

    return df