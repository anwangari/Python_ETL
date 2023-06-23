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
