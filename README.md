# Python ETL
In this project, I developed a custom python ETL class to automate scraping of historic forex data from Alpha Vintage API, transform, and load the data into a SQL database (SQLite).

## Description
### 1. `config.py`
`config.py` serves as a configuration module for storing sensitive information. It searches for a `.env` file and reads its contents

### 2. `API.ipynb`
This notebook showcases API integration and data manipulation using Python and Pandas. It also shows the iterative process of building the `data.py` module

### 3. `data.py`
The `data.py` module provides a class `API` that **EXTRACT and TRANSFORM** foreign exchange data from the Alpha Vantage API and returns it as a clean Pandas DataFrame. class `SQLRepo` handles **LOAD** - from the dataframe to a SQL database; and pulling data from the SQL database (Data Warehouse) for further processing/analysis
