import psycopg2
import pandas as pd

def connect_to_postgresql(host, port, database, user, password):
   

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Example usage:
host = "localhost"
port = 5432  # Default PostgreSQL port
database = "telecom"
user = "postgres"
password = "post@5432"

conn = connect_to_postgresql(host, port, database, user, password)
def read_data(conn):
   # """
   # Retrieves data from a table.
   # """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM xdr_data")
    results = cursor.fetchall()
   # cursor.close()
    return results

if conn:
    print("Connected to PostgreSQL successfully!")
    # Perform database operations here
    read_data(conn)
    df = pd.DataFrame(read_data(conn))

    #conn.close()
else:
    print("Failed to connect to PostgreSQL.")


    # Example query

# Convert the result to a Pandas DataFrame
#df = pd.DataFrame(read_data(conn))
print(df.head())  # Display the first few rows of the DataFrame
conn.close()
print(df.describe)

#from src.utils import missing_values_table, convert_bytes_to_megabytes


