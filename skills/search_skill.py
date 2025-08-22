import requests

def search(query):
    # Simple fallback using DuckDuckGo Instant Answer API
    url = f"https://api.duckduckgo.com/?q={query}&format=json&lang=sq"
    r = requests.get(url).json()
    if r.get("AbstractText"):
        return r["AbstractText"]
    return "Më vjen keq, nuk gjeta një përgjigje."
