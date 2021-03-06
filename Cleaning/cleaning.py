import pandas as pd
import requests
import numpy as np

def api_read(city_list,limit, key, url):
    frame = pd.DataFrame()
    """
    Function that will take a list of cities, limit, key, url, and empty dataframe and will create a dataframe
    Add convert dataframe into csv for further use later
    """
    for city in city_list:
        querystring = {"state_code":"CA","city":city,"limit":"200","offset":"0","sort":"sold_date"}
        headers = {
            'x-rapidapi-host': "us-real-estate.p.rapidapi.com",
            'x-rapidapi-key': key
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        for i in range(limit):
            row = data['data']['results'][i]['description']
            row['list_price'] = data['data']['results'][i]['list_price']
            row['city'] = city
            frame=frame.append(row , ignore_index=True)
    return frame

#code gotten from stackoverflow
def recode_empty_cells(dataframe, list_of_columns):

    for column in list_of_columns:
      dataframe[column] = dataframe[column].replace(r'\s+', np.nan, regex=True)
      dataframe[column] = dataframe[column].fillna(0)


"""
df = api_read(cities,200,key,url)
print(df)
"""