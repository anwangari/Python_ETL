# FX-Market-Forecasting
In this project, I am developing a custom python ETL class to automate scraping of historic forex data from Alpha Vintage API, transform and load the data into a SQL database (SQLite).
I will also make a prediction model to predict future price / volatility, and make a simple web app to serve my model’s predictions

## Description
### 1. Configuration Module: `config.py`
`config.py` serves as a configuration module for storing sensitive information. It searches for a `.env` file and reads its contents

### 2. `API.ipynb`
This notebook fetches currency exchange data from an API, converts it into a Pandas DataFrame, and performs data cleaning. It demonstrates the installation of libraries, constructing the API URL, sending requests, extracting the data, converting the index to DateTime format, and cleaning column names. The notebook also includes a function and a class for automating the data retrieval process. It showcases API integration and data manipulation using Python and Pandas.

### 
