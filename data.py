import pandas as pd
import requests
from config import settings

class API:
    def __init__(self, key=settings.api_key):
        
        self.__api_key = key
        
    def get_api_data(self, currency_from="USD", currency_to="KES", output_size="full"):
        # create url
        url = (
          "https://www.alphavantage.co/query?"
          "function=FX_DAILY&"
          f"from_symbol={currency_from}&"
          f"to_symbol={currency_to}&"
          f"outputsize={output_size}&"
          f"apikey={self.__api_key}"
          )
        # send request to API
        response = requests.get(url)

        # extract json data from response
        response_data = response.json()

        # put data in a dataframe
        ## data validation step
        if "Time Series FX (Daily)" not in response_data.keys():
            raise Exception(
              f"Invalid API call: check that currency_from sysmbol: '{currency_from}' and currency_to symbol: '{currency_to}' are correct"
          )

        fx_data = response_data['Time Series FX (Daily)']
        df = pd.DataFrame.from_dict(fx_data, orient="index", dtype=float)

        # convert index to datetime fomat: name index as 'date'
        df.index = pd.to_datetime(df.index)
        df.index.name = "date"

        # clean column names
        df.columns = [c.split(". ")[1] for c in df.columns]

        return df

class SQLRepo:
    def __init__(self, connection=sqlite3.connect(settings.db_name, check_same_thread=False)):
        
        self.connection = connection
        
    def load_data(self, records, currency_from="USD", currency_to="KES", if_exists="fail"):
        table_name = f"{currency_from}{currency_to}"
        # read data to database
        n_records = records.to_sql(name=table_name, con=self.connection, if_exists=if_exists)

        return {
          "Table Name: ": table_name,
          "Number of records updated" : n_records
          }
    
    def get_sql_data(self, currency_from="USD", currency_to="KES", limit=None):
        # define query
        if limit:
            query = f"SELECT * FROM {currency_from}{currency_to} limit {limit}"
        else:
            query = f"SELECT * FROM {currency_from}{currency_to}"

        # read data from database
        df = pd.read_sql(
            sql=query,
            con=self.connection,
            parse_dates=["date"],
            index_col="date"
            )

        return df
