from csv import reader
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_weather():
    try:
        ResultBytes = request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Limassol?unitGroup"
            "=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv").read().decode('UTF-8')
        # print('ResultBytes', ResultBytes)
        array = ResultBytes.splitlines()
        tableData = []
        for line in reader(array):
            tableData.append(line)

        dfColumns = ['Περιοχή', 'Ημερομηνία', 'Θερμοκρασία', 'Μικρότερη', 'Μεγαλύτερη']
        dfRows = []
        for lineIndex in range(1, len(tableData)):
            dfRows.append([tableData[lineIndex][0],
                           tableData[lineIndex][1],
                           tableData[lineIndex][4],
                           tableData[lineIndex][3],
                           tableData[lineIndex][2]])
        return pd.DataFrame(data=dfRows, columns=dfColumns)

    except error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except error.URLError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()


dfResult = getWeather()
print(dfResult)
