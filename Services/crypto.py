from csv import reader
import json
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_crypto():
    try:
        result_bytes = request.urlopen(
            "https://api.coinstats.app/public/v1/coins?skip=0&limit=20&currency=EUR").read().decode('UTF-8')
        array = result_bytes.splitlines()
        dictionary = json.loads(array[0])

        coins_array = json.loads(array[0])
        pd_df = pd.DataFrame.from_dict(coins_array)
        coins_from_pd_df = pd_df['coins']
        expanded_coins = (coins_from_pd_df.explode().tolist())

        data_frame = pd.DataFrame.from_dict(dictionary)

        df_from_df = pd.DataFrame.from_records(coins_array)

        data_rows = []

        for ind in data_frame.index:
            data_rows.append(data_frame.loc[ind]['coins'])

        custom_columns = ['name', 'symbol', 'price', 'priceChange1h', 'priceChange1d', 'priceChange1w']

        refined_data_frame = pd.DataFrame(data=data_rows, columns=custom_columns)

        # renaming the DataFrame columns
        refined_data_frame.rename(columns={
            'name': 'Όνομα',
            'symbol': 'Σύμβολο',
            'price': 'Αξία ($)',
            'priceChange1h': 'Αυξομείωση 1 ώρα',
            'priceChange1d': 'Αυξομείωση 1 ημέρα',
            'priceChange1w': 'Αυξομείωση 1 εβδομάδα',
        },
            inplace=True)

        return refined_data_frame

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_crypto()
