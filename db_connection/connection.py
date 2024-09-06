import psycopg2

def connect_to_postgresql(host, port, database, user, password):
    """
    Connects to a PostgreSQL database and returns a connection object.

    Args:
        host (str): The hostname of the PostgreSQL server.
        port (int): The port number of the PostgreSQL server.
        database (str): The name of the database to connect to.
        user (str): The username to use for authentication.
        password (str): The password to use for authentication.

    Returns:
        psycopg2.connect: A connection object to the PostgreSQL database.
    """

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
        print("Error connecting to PostgreSQL:", e)
        return None

# Example usage:
host = "localhost"
port = 5432  # Default PostgreSQL port
database = "telecom"
user = "postgres"
password = "post@5432"

conn = connect_to_postgresql(host, port, database, user, password)

if conn:
    # Use the connection object to execute SQL queries
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
else:
    print("Failed to connect to PostgreSQL.")