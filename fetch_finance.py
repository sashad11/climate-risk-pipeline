import yfinance as yf
import duckdb
import pandas as pd

def fetch_and_clean_finance_data():
    print("Connecting to the London Stock Exchange feed...")
    
    # 1. Download the last 7 days of daily market data for National Grid plc
    ticker_symbol = "NG.L"
    stock_engine = yf.Ticker(ticker_symbol)
    df_raw = stock_engine.history(period="7d")
    
    print("Shaping and cleaning stock table structure...")
    
    # 2. Reset the date row layout and extract the core columns we need
    df_raw = df_raw.reset_index()
    df_clean = pd.DataFrame()
    df_clean['market_date'] = pd.to_datetime(df_raw['Date']).dt.date
    df_clean['closing_price_pence'] = df_raw['Close'].astype(float)
    df_clean['trading_volume'] = df_raw['Volume'].astype(int)
    
    print("Saving financial data into your DuckDB cabinet...")
    
    # 3. Connect to our central project vault database and create a table
    connection = duckdb.connect("carbon_analytics.db")
    connection.execute("CREATE OR REPLACE TABLE clean_finance_metrics AS SELECT * FROM df_clean")
    
    print("\n--- Visual Verification Check (DuckDB Finance Table Preview) ---")
    print(connection.execute("SELECT * FROM clean_finance_metrics").fetchdf())
    
    connection.close()

if __name__ == "__main__":
    fetch_and_clean_finance_data()