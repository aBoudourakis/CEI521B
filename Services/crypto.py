from csv import reader
import json
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_crypto():
    try:
        result_bytes = request.urlopen(
            "https://api.coinstats.app/public/v1/coins?skip=0&limit=5&currency=EUR").read().decode('UTF-8')
        # print('result_bytes', result_bytes)
        array = result_bytes.splitlines()
        print('array', array)
        print('array[0]', array[0])
        dictionary = json.loads(array[0])
        print('dictionary', dictionary['coins'])
        print('type dictionary', type(dictionary['coins']))

        coins_array = json.loads(array[0])
        pd_df = pd.DataFrame.from_dict(coins_array)
        coins_from_pd_df = pd_df['coins']
        expanded_coins = (coins_from_pd_df.explode().tolist())
        print('expanded_coins', expanded_coins)

        data_frame = pd.DataFrame.from_dict(dictionary)
        print('data_frame type', type(data_frame))
        print('data_frame', data_frame)

        print('test locate row', data_frame.loc[0])
        print('test locate row type', type(data_frame.loc[0]))

        df_from_df = pd.DataFrame.from_records(coins_array)
        print('df_from_df', df_from_df)

        # merged_dataframe = pd.DataFrame(data=dictionary, columns=expanded_coins)
        # print('merged_dataframe', merged_dataframe)

        print('=====================')

        data_rows = []

        for ind in data_frame.index:
            data_rows.append(data_frame.loc[ind]['coins'])
            # print(data_frame.loc[ind]['coins'])

        print('data_rows', data_rows)

        custom_columns = ['name', 'price']

        variables = data_rows[0].keys()
        print('variables', variables)
        df_test = pd.DataFrame(data=data_rows, columns=custom_columns)

        # renaming the DataFrame columns
        df_test.rename(columns={'name': 'Όνομα',
                                'price': 'Τιμή ($)'},
                       inplace=True)

        print('df_test', df_test)

        return df_test

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_crypto()
print(dfResult)
