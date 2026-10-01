import duckdb

def merge_analytics_tables():
    print("Connecting to DuckDB storage vault...")
    connection = duckdb.connect("carbon_analytics.db")
    
    print("Merging climate risk exposure matrix with financial data...")
    
    # Write a SQL query to average carbon readings by date and JOIN with stock prices
    sql_query = """
        CREATE OR REPLACE TABLE final_dissertation_dataset AS
        SELECT 
            f.market_date,
            f.closing_price_pence,
            f.trading_volume,
            ROUND(AVG(c.carbon_actual_intensity), 2) AS avg_daily_carbon_intensity,
            MODE(c.emission_level_rating) AS primary_emission_rating
        FROM clean_finance_metrics f
        JOIN clean_carbon_metrics c
          ON f.market_date = CAST(c.reading_time AS DATE)
        GROUP BY f.market_date, f.closing_price_pence, f.trading_volume;
    """
    
    connection.execute(sql_query)
    print("Pipeline successfully unified! Created final composite table.")
    
    print("\n--- Final Project Dataset Preview (Your Completed Model) ---")
    print(connection.execute("SELECT * FROM final_dissertation_dataset").fetchdf())
    
    connection.close()

if __name__ == "__main__":
    merge_analytics_tables()