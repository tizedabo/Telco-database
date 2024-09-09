
import os
import sys
import pandas as pd  
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from DB_connection.connection import PostgresConnection

current_dir = os.getcwd()
print(current_dir)

# Get the parent directory
parent_dir = os.path.dirname(current_dir)
print(parent_dir)

# Insert the path to the parent directory
sys.path.insert(0, parent_dir)

st.set_page_config(page_title="Tellco Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ data from DATABASE ----

db = PostgresConnection(dbname='telecom', user='postgres', password='post@5432')
db.connect()

# Example query
query = "SELECT * FROM xdr_data"
result = db.execute_query(query)

# Convert the result to a Pandas DataFrame
df = pd.DataFrame(result, columns=[desc[0] for desc in db.cursor.description])
print(df.head())  # Display the first few rows of the DataFrame

# Close the connection when done
db.close_connection()
st.write("Tellco Dashboards")
st.write(df)