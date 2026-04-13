import os
from typing import List, Optional
import requests
from pydantic import parse_obj_as
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

headers = {
    "apikey": SUPABASE_ANON_KEY,
    "Content-Type": "application/json",
    "Prefer": "return=minimal",
}


def query_table(table: str, filters: dict = None) -> List[dict]:
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    params = {}
    if filters:
        for k, v in filters.items():
            params[k] = f"eq.{v}"
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()


def insert_row(table: str, data: dict) -> dict:
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()


def update_row(table: str, row_id: str, data: dict) -> dict:
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    params = {"id": "eq." + row_id}
    resp = requests.patch(url, headers=headers, json=data, params=params)
    resp.raise_for_status()
    return resp.json()