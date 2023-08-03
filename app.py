from flask import Flask, render_template
import pyodbc
import os

app = Flask(__name__)

# Configura la conexión a la base de datos
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

# Intenta establecer la conexión a la base de datos
try:
    conn_str = ";".join([f"{key}={value}" for key, value in config.items()])
    conn = pyodbc.connect(conn_str)
    print("Conexión exitosa a la base de datos")

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

except pyodbc.Error as error:
    print(f"Error al conectar a la base de datos: {error}")
    conn = None
    cursor = None

@app.route('/')
def index():
    print('Request for index page received')

    try:
        if conn:
            # Realiza una consulta a la base de datos para obtener los datos de coches
            cursor.execute("SELECT * FROM coches")
            results = cursor.fetchall()
            database_connected = True
        else:
            results = []
            database_connected = False
    except pyodbc.Error as error:
        print(f"Error al obtener los datos de coches: {error}")
        results = []
        database_connected = False

    return render_template('index.html', results=results, database_connected=database_connected)

if __name__ == '__main__':
    app.run()
