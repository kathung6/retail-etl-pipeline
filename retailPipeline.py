import psycopg2

conn = psycopg2.connect(
    dbname = "retail_db",
    user="your_user",
    password = "your_password",
    host = "localhost",
    port = "5432"
)

SELECT * FROM grocery_sales

import pandas as pd
import os

#extract function
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

merged_df = extract(grocery_sales, "extra_data.parquet")

def transform(raw_data):
    