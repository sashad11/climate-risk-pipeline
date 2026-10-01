import os
import requests

# The official National Grid API endpoint
API_URL = "https://api.carbonintensity.org.uk/intensity"

def fetch_carbon_data():
    print("Connecting to the UK Carbon Intensity API...")
    
    # This header is vital! It tells the server we are a database, not a webpage
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        # Grab the response as a clean Python dictionary structure
        json_data = response.json()
        
        print("Data downloaded successfully! Let's verify the layout:")
        print(json_data)  # This will print the raw rows to your terminal screen
        
        # Save the file using the standard python json tools to ensure it formats perfectly
        import json
        with open("raw_carbon_data.json", "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)
            
        print("Raw data cleanly saved to 'raw_carbon_data.json'!")
    else:
        print(f"Failed to fetch data. Error code: {response.status_code}")

if __name__ == "__main__":
    fetch_carbon_data()