# src/insert_data.py

import pandas as pd
import psycopg2
from db_config import DB_PARAMS

# Read CSV data
df = pd.read_csv('data\\stock_data.csv')

# Connect to the PostgreSQL database
conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

# Create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS stock_data (
    datetime TIMESTAMP,
    close DECIMAL,
    high DECIMAL,
    low DECIMAL,
    open DECIMAL,
    volume INTEGER,
    instrument VARCHAR(50)
);
"""
cur.execute(create_table_query)

# Insert data into the table
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO stock_data (datetime, close, high, low, open, volume, instrument)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(insert_query, tuple(row))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

print("Data inserted successfully.")
