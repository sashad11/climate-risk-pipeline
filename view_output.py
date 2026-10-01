import duckdb

# Connect to your local database file
connection = duckdb.connect("carbon_analytics.db")

print("Exporting your final database table to a standard CSV spreadsheet...")

# Tell DuckDB to copy your final dataset into a readable spreadsheet file
connection.execute("COPY final_dissertation_dataset TO 'final_output_spreadsheet.csv' (HEADER, DELIMITER ',');")

print("Export complete! You now have a visible spreadsheet file.")
connection.close()