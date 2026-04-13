import requests
from typing import List

AI_SERVICE_URL = "https://your-sasl-model.example.com/predict"


def run_sasl_ocr(video_url: str, start_sec: float, end_sec: float) -> List[dict]:
    payload = {
        "video_url": video_url,
        "start_sec": start_sec,
        "end_sec": end_sec,
    }
    resp = requests.post(AI_SERVICE_URL, json=payload)
    resp.raise_for_status()
    return resp.json()["segments"]  # list of {start, end, english_text, saslgloss}