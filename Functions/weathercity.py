from csv import reader
import sys
from urllib import request
from urllib import error
import pandas as pd


def refine_temperature_display(temp_value):
    refined_value = str(temp_value) + '°'
    return refined_value


def normalize_date(date_value):
    splitDate = date_value.split('-')
    splitDate.reverse()
    refined_date = '/'.join(splitDate)
    return refined_date


def get_weather_by_input(input):
    try:
        url_string = "https://cei521athinodoros.azurewebsites.net/api/WeatherProxy?code=rcDbnyCDmfNgZR0eFlvEqFEtXwKOQ1r1bI4HVFI6XESRAzFu6bz3Bw==&city=" + input
        result_bytes = request.urlopen(url_string).read().decode('UTF-8')
        array = result_bytes.splitlines()
        table_data = []
        for line in reader(array):
            table_data.append(line)

        df_columns = ['Περιοχή', 'Ημερομηνία', 'Θερμοκρασία (°C)', 'Μικρότερη (°C)', 'Μεγαλύτερη (°C)']
        df_rows = []
        for lineIndex in range(1, len(table_data)):
            df_rows.append([table_data[lineIndex][0],
                            normalize_date(table_data[lineIndex][1]),
                            refine_temperature_display(table_data[lineIndex][4]),
                            refine_temperature_display(table_data[lineIndex][3]),
                            refine_temperature_display(table_data[lineIndex][2])
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

