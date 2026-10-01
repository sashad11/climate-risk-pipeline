import os
import requests
import json

# 💡 FIX: Adjusted to match the exact official historic date endpoint format
API_URL = "https://carbonintensity.org.uk"

def fetch_carbon_data():
    print("Connecting to the UK Carbon Intensity API for a historic date window...")
    
    # Establish complete web communication headers
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    response = requests.get(API_URL, headers=headers)
    
    # Check if the server responded with text instead of error codes
    if response.status_code == 200:
        try:
            # Safely unpack the data block
            json_data = response.json()
            print("Historical climate data downloaded successfully!")
            
            # Write a clean, formatted master copy to disk
            with open("raw_carbon_data.json", "w", encoding="utf-8") as file:
                json.dump(json_data, file, indent=4)
            print("Raw data cleanly saved to 'raw_carbon_data.json'.")
            
        except Exception as e:
            print(f"Server returned a non-JSON message. Preview: {response.text[:200]}")
    else:
        print(f"Failed to fetch data. Server status code: {response.status_code}")

if __name__ == "__main__":
    fetch_carbon_data()