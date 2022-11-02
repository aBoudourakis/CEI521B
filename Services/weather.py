from csv import reader
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_weather():
    try:
        result_bytes = request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Limassol?unitGroup"
            "=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv").read().decode('UTF-8')
        # print('ResultBytes', ResultBytes)
        array = result_bytes.splitlines()
        table_data = []
        for line in reader(array):
            table_data.append(line)

        df_columns = ['Περιοχή', 'Ημερομηνία', 'Θερμοκρασία', 'Μικρότερη', 'Μεγαλύτερη']
        df_rows = []
        for lineIndex in range(1, len(table_data)):
            df_rows.append([table_data[lineIndex][0],
                           table_data[lineIndex][1],
                           table_data[lineIndex][4],
                           table_data[lineIndex][3],
                           table_data[lineIndex][2]])
        return pd.DataFrame(data=df_rows, columns=df_columns)

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_weather()
print(dfResult)
