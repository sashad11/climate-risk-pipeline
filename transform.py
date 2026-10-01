import pandas as pd
import json
import duckdb

def clean_and_shape_data():
    print("Opening your raw data file...")
    
    # 1. Open and load the text data from your json file
    with open("raw_carbon_data.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)
    
    # 2. Extract the nested list under the "data" key
    raw_list = json_data["data"]
    
    print("Shaping the data using Excel-style frames (Pandas)...")
    
    # 3. Flatten the dictionary layer into columns instantly
    df = pd.json_normalize(raw_list)
    
    # 4. Give the columns beautiful, clear names for your project
    df_clean = pd.DataFrame()
    df_clean['reading_time'] = pd.to_datetime(df['from'])
    df_clean['ending_time'] = pd.to_datetime(df['to'])
    df_clean['carbon_forecast_intensity'] = df['intensity.forecast'].astype(int)
    df_clean['carbon_actual_intensity'] = df['intensity.actual'].astype(int)
    df_clean['emission_level_rating'] = df['intensity.index'].str.strip().str.lower()
    
    print("Data successfully cleaned! Saving into your DuckDB cabinet...")
    
    # 5. Save this perfect data directly into DuckDB table format
    connection = duckdb.connect("carbon_analytics.db")
    connection.execute("CREATE OR REPLACE TABLE clean_carbon_metrics AS SELECT * FROM df_clean")
    
    # 6. Print out your visual preview table in the terminal!
    print("\n--- Visual Verification Check (DuckDB Table Preview) ---")
    print(connection.execute("SELECT * FROM clean_carbon_metrics").fetchdf())
    
    connection.close()

if __name__ == "__main__":
    clean_and_shape_data()