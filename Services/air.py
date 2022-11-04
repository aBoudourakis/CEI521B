from csv import reader
import json
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_pollution():
    try:
        result_bytes = request.urlopen(
            "https://api.waqi.info/feed/here/?token=6991a7e7db2339c3304b0bbf7e057effbb1e98f8").read(

        ).decode(
            'UTF-8')
        # print('result_bytes', result_bytes)
        dictionary = json.loads(result_bytes)
        # print('dictionary', dictionary)
        # print('data', dictionary['data'])
        # print('data target', dictionary['data']['iaqi'])

        cityData = dictionary['data']['city']
        # print('cityData', cityData)
        print('cityData', cityData['name'])
        greek_city_info = cityData['name'].split(',')[1]
        city_info = greek_city_info.split('  ')[0]
        print('greek_city_info', greek_city_info)
        print('city_info', city_info)
        pollution = dictionary['data']['iaqi']

        valuesArray = []

        table_columns = ['Ρύπος', 'Τιμή']
        table_rows = []

        for key in pollution:
            # table_columns.append(key)
            table_rows.append([key, pollution[key]['v']])
            valuesArray.append({key: pollution[key]['v']})
        # for index in range(1, len(valuesArray)):
        #     table_rows.append([index, valuesArray[index]])

        # print('array values', valuesArray)
        # print('table_columns', table_columns)
        # print('table_rows', table_rows)
        # TODO: convert above to data frame (series of tuples/key-value pairs array?

        return [city_info, pd.DataFrame(data=table_rows, columns=table_columns)]

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_pollution()
print(dfResult)
