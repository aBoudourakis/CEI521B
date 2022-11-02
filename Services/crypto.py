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
        print(array)
        coins_array = json.loads(array[0])
        print(coins_array)
        print(type(coins_array))
        pd_df = pd.DataFrame.from_dict(coins_array)
        print(type(pd_df))
        print('pd_df')
        print(pd_df)
        print('=================')
        print(pd_df.iloc[0])
        print('type(testPdDf.iloc[0])')
        print(type(pd_df.iloc[0]))
        item_test = pd_df.iloc[0]
        print("item_test['argss]")
        # below extraction from df series works --> look into iterating/mapping all series
        print(item_test['coins']['name'])
        test_all = pd_df['coins']
        print('test_all')
        print(test_all)
        print(type(test_all))
        expanded_test_all = (test_all.explode().tolist())
        # expandedTestAll = pd.DataFrame(pd.Series(testAll).explode().tolist()).drop('id', 1)
        print('expandedTestAll')
        print(expanded_test_all)
        # print(expanded_test_all)
        # next line works and extracts id value
        # TODO look further into constructing desired table like weather service
        print('extract data from index of row 1')
        print(item_test[0]["id"])
        print(item_test[0]["name"])
        print(item_test[0]["symbol"])
        print(item_test[0]["icon"])
        print(item_test[0]["price"])
        print(item_test[0]["priceChange1h"])
        print(item_test[0]["priceChange1d"])
        print(item_test[0]["priceChange1w"])
        print(pd_df.iloc[1])

        # array = coins_array.splitlines()
        array = pd_df

        table_data = []
        for line in reader(coins_array):
            table_data.append(line)

        # construct data frame
        df_columns = ['Όνομα', 'Σύμβολο', 'Λογότυπο', 'Τιμή ($)', 'Αυξομείωση 1 ώρα', 'Αυξομείωση 1 ημέρα',
                      'Αυξομείωση 1 εβδομάδα']
        df_rows = []
        for lineIndex in range(1, len(table_data)):
            df_rows.append([
                item_test[lineIndex]["name"],
                item_test[lineIndex]["symbol"],
                item_test[lineIndex]["icon"],
                item_test[lineIndex]["price"],
                item_test[lineIndex]["priceChange1h"],
                item_test[lineIndex]["priceChange1d"],
                item_test[lineIndex]["priceChange1w"],
            ])
        return pd.DataFrame(data=df_rows, columns=df_columns)

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
