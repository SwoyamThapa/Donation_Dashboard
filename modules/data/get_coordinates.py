import pandas as pd
import plotly.graph_objects as go
import requests

# Your OpenCage Data API key
api_key = "c1da6c6cae66404ba1db0b1399c97e7d"

# Function to get coordinates for a country
def get_coordinates(country_name):
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": country_name,
        "key": api_key,
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data and "results" in data:
            result = data["results"][0]
            lat = result["geometry"]["lat"]
            lon = result["geometry"]["lng"]
            return lat, lon

    return None, None

# The rest of your code remains the same
# ...
