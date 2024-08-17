# utils/http_headers.py

import requests

def fetch_http_headers(url):
    try:
        print("Fetching HTTP headers...")
        headers = requests.head(url).headers
        for header, value in headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"Failed to fetch HTTP headers: {e}")
