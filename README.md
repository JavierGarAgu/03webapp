# Azure Web App - Python Quickstart

## Overview

This project is a Python web application prepared to run on an Azure Web App with Python 3.9. The application uses Flask as the web framework and retrieves data from an Azure SQL Database to display a list of cars.

## Technologies Used

- Python: The backend of the web application is written in Python using Python 3.9.
- Flask: Flask is a lightweight web framework for Python that allows us to easily create web applications.
- Azure SQL Database: The data for this application is stored in an Azure SQL Database, which is a fully managed relational database service provided by Microsoft Azure.
- Azure Web App: The application is deployed and hosted on an Azure Web App, which allows us to run web applications in the cloud.

## Prerequisites

Before deploying the application to an Azure Web App, ensure you have the following prerequisites:

1. An Azure account: You will need an Azure account to create and manage Azure resources.
2. Azure SQL Database: Set up an Azure SQL Database with the required tables and data. Make sure to obtain the connection details.
3. Azure Web App: Create an Azure Web App with Python 3.9 runtime support.

Or you can use my terraform file for create the infraestructure: https://github.com/JavierGarAgu/terraform/tree/master/03

## How the Application Works

1. The application uses the `pyodbc` library to establish a connection to the Azure SQL Database using the provided connection details.

2. The `index` route in the Flask app fetches data from the "coches" table in the Azure SQL Database using a SQL query.

3. If the database connection is successful, the retrieved data (list of cars) is displayed on the homepage of the web application using an HTML table.

4. If there is an error in the database connection or fetching data from the database, an error message is displayed on the homepage indicating that the application couldn't connect to the database.

## Additional Notes

- The `index.html` file in the `templates` folder contains the HTML template for the homepage of the web application. The template uses Jinja2 templating syntax to dynamically render the list of cars fetched from the database.

- Make sure to handle database connection errors gracefully and implement proper error handling in production environments.

- This application is intended for deployment to an Azure Web App and may require additional security and optimization measures for production use.

Feel free to explore and modify the code to suit your specific requirements. If you encounter any issues or have any questions, don't hesitate to reach out for support. Happy coding!
