#TODO fix table names to get only the part after "\"

import pandas as pd
import sqlite3
import glob  # To get all CSV files in a directory

# Define the SQLite database file
db_file = "data/my_database.db"

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Get all CSV files in the current directory
csv_files = glob.glob("C:/Users/Owner/Documents/GitHub/ml_footballer_transfer_predictor/data/*.csv")  # Change path if needed

for file in csv_files:
    # Read CSV file
    df = pd.read_csv(file)
    
    # Use filename (without extension) as table name
    table_name = file.split(".")[0]  
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    
    print(f"✔ Loaded {file} into {table_name} table.")

# Close connection
conn.close()
print("All files imported successfully into SQLite!")