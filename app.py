import os
import pyodbc
from flask import Flask, redirect, render_template, request, send_from_directory, url_for

app = Flask(__name__)

# Configura la conexión a la base de datos
config = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': 'jga.database.windows.net',
    'database': 'coches',
    'uid': 'jga',
    'pwd': '1234!Strong',
    'Encrypt': 'yes',
    'TrustServerCertificate': 'no',
    'Connection Timeout': 30
}

# Función para obtener una conexión a la base de datos
def get_db_connection():
    conn_str = ";".join([f"{key}={value}" for key, value in config.items()])
    return pyodbc.connect(conn_str)

@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/coches')
def coches():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM coches')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('coches.html', data=data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name=name)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
