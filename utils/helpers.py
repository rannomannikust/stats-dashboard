import requests
import logging
#from pathlib import Path
#from dotenv import load_dotenv, find_dotenv

import os
from openai import OpenAI, api_key
from typing import Optional


_log = logging.getLogger(__name__)
_client: Optional[OpenAI] = None

def set_openai_client(client: OpenAI) -> None:
    global _client
    _client = client

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY puudub — kontrolli .env ja load_dotenv teed")
    return OpenAI(api_key=api_key)

def ask_gpt(user_text: str) -> str:
    """
    Küsib GPT-lt vastuse antud tekstile ja tagastab stringi. 
    Kui API kutse ebaõnnestub, tagastab viisaka veateate.
    """
    if _client is None:
        raise RuntimeError("OpenAI client pole määratud. Kutsu set_openai_client(app_client) enne ask_gpt.")
    try:
        response = _client.responses.create(
            model="gpt-4.1-mini",
            input=user_text
        )
        return response.output[0].content[0].text
    except Exception as e: # logime vea serveri poolel, et arendaja näeks
        _log.error("GPT API error: %s", exc_info=e)
        return "Vabandust, praegu ei õnnestu GPT-lt vastust saada. Proovi hiljem uuesti."


def apply_common_legend(fig, orientation, y, x, yanchor="bottom", xanchor="center"):
    """Lisa graafikule ühtne legendi paigutus (alla keskele)."""
    fig.update_layout(
        legend=dict(
            orientation= orientation,
            yanchor=yanchor,
            y=y,
            xanchor=xanchor,
            x=x
        )
    )
    return fig

# Abifunktsioon metaandmete jaoks

def get_meta_options(table="PA103", lang="et"):
    url = f"https://andmed.stat.ee/api/v1/{lang}/stat/{table}"
    meta = requests.get(url).json()

    opts = {}
    for v in meta["variables"]:
        code = v["code"]
        values = v["values"]
        labels = v["valueTexts"]
        opts[code] = [{"label": lbl, "value": val} for val, lbl in zip(values, labels)]
    return opts