# FX-Market-Forecasting
In this project, I am developing a custom python ETL class to automate scraping of historic forex data from Alpha Vintage API, transform and load the data into a SQL database (SQLite).
I will also make a prediction model to predict future price / volatility, and make a simple web app to serve my model’s predictions

## Description
### 1. `config.py`
`config.py` serves as a configuration module for storing sensitive information. It searches for a `.env` file and reads its contents

### 2. `API.ipynb`
This notebook showcases API integration and data manipulation using Python and Pandas.

### 3. `data.py`
The `data.py` module provides a class `API` that **EXTRACT and TRANSFORM** foreign exchange data from the Alpha Vantage API and returns it as a clean Pandas DataFrame.
