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
        # print('input', input)
        # result_bytes = request.urlopen(input)
        url_string = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + input + "?unitGroup=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv"
        # url_string.append(input)
        # url_string.append('Moscow')
        # url_string.append("?unitGroup=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv")
        result_bytes = request.urlopen(url_string).read().decode('UTF-8')
        # print('result_bytes', result_bytes)

        array = result_bytes.splitlines()
        table_data = []
        for line in reader(array):
            table_data.append(line)

        df_columns = ['Περιοχή', 'Ημερομηνία', 'Θερμοκρασία (°C)', 'Μικρότερη (°C)', 'Μεγαλύτερη (°C)']
        df_rows = []
        for lineIndex in range(1, len(table_data)):
            # originalDate = table_data[lineIndex][1].split('-')
            # refinedDate = '/'.join(originalDate)

            df_rows.append([table_data[lineIndex][0],
                            normalize_date(table_data[lineIndex][1]),
                            refine_temperature_display(table_data[lineIndex][4]),
                            refine_temperature_display(table_data[lineIndex][3]),
                            refine_temperature_display(table_data[lineIndex][2])
                            ])

        # print('data_frame', data_frame)
        return pd.DataFrame(data=df_rows, columns=df_columns)

        # return input

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_weather_by_input('CHECK')
print(dfResult)
