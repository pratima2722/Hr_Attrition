import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
)

query = "SELECT * FROM HR_ATTRITION.RAW.HR_ATTRITION_FINAL LIMIT 10"

df = pd.read_sql(query, conn)

print("Data shape:", df.shape)
print(df.head())

conn.close()