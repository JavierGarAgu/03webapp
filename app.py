from flask import Flask, render_template
import pyodbc
import os

app = Flask(__name__)

# Configure the database connection
config = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': os.environ.get('APPSETTING_SERVER'),
    'database': os.environ.get('APPSETTING_DB'),
    'uid': os.environ.get('APPSETTING_USER'),
    'pwd': os.environ.get('APPSETTING_PASSWORD'),
    'Encrypt': 'yes',
    'TrustServerCertificate': 'no',
    'Connection Timeout': 30
}

# Attempt to establish the database connection
try:
    conn_str = ";".join([f"{key}={value}" for key, value in config.items()])
    conn = pyodbc.connect(conn_str)
    print("Successful connection to the database")

    # Create a cursor to execute queries
    cursor = conn.cursor()

except pyodbc.Error as error:
    print(f"Error connecting to the database: {error}")
    conn = None
    cursor = None

@app.route('/')
def index():
    print('Request for index page received')

    try:
        if conn:
            # Execute a query to retrieve data from the 'coches' table in the database
            cursor.execute("SELECT * FROM coches")
            results = cursor.fetchall()
            database_connected = True
        else:
            results = []
            database_connected = False
    except pyodbc.Error as error:
        print(f"Error fetching data from coches table: {error}")
        results = []
        database_connected = False

    # Get the user from the environment variable APPSETTING_USER
    user = os.environ.get('APPSETTING_USER', 'User')

    return render_template('index.html', results=results, database_connected=database_connected, user=user)

if __name__ == '__main__':
    app.run()
