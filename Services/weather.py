import csv
import re
from csv import reader
import sys
from urllib import request
from urllib import error
import pandas as pd
import streamlit as st
import numpy as np

try:
    ResultBytes = request.urlopen(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Limassol?unitGroup"
        "=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv").read().decode('UTF-8')
    print('ResultBytes', ResultBytes)
    # Parse the results as CSV
    # CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
    # Parse the results as JSON
    # jsonData = json.loads(ResultBytes.decode('utf-8'))
    # TODO map data onto the table below
    # print('ResultBytes[0]', ResultBytes[1])
    # results = []
    # with ResultBytes as csvfile:
    #     reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
    #     for row in reader:  # each row is a list
    #         results.append(row)
    #
    # print('results', results)
    array = ResultBytes.splitlines()
    tableData = []
    for line in reader(array):
        tableData.append(line)
        # print('line', line)
    # print('tableData', tableData)

    # dfColumns = [tableData[0][0], 'Time', tableData[0][4]]
    dfColumns = ['Περιοχή', 'Ώρα', 'Θερμοκρασία']
    defRows = []
    for lineIndex in range(1, len(tableData)):
        defRows.append([tableData[lineIndex][0], tableData[lineIndex][1], tableData[lineIndex][4]])
    print('dfColumns', dfColumns)
    print('defRows', defRows)

    # pandasDF = pd.DataFrame({
    #
    # })
    # print('array', array)
    # print('len(array[0])', len(array[0]))
    #             tableArray = []
    #             for row in array:
    #                 # print('row', row.split(r'(?:^"?|, ?"?)\K(?:(?<=").+?(?=")|[\w-]+)'))
    #                 splitRow = row.split(r'(?:^"?|, ?"?)\K(?:(?<=").+?(?=")|[\w-]+)')
    #                 print('splitRow[0]', splitRow[0])
    #                 tableArray.append(splitRow)
    # print('row', re.split(r'"[^"]*"(*SKIP)(*FAIL)|,\s*', row))
    # print('row', rx.split(row))
    # print('tableArray', tableArray[1])
    # arrayedRow = str(tableArray[1]).split(r'(?:^"?|, ?"?)\K(?:(?<=").+?(?=")|[\w-]+)')
    # print('arrayedRow', arrayedRow)
    # print('tableArray split row?', str(tableArray[1]).split(r'(?:^"?|, ?"?)\K(?:(?<=").+?(?=")|[\w-]+)'))
    # print('tableArray split?', tableArray[1].split(r'(?:^"?|, ?"?)\K(?:(?<=").+?(?=")|[\w-]+)'))
    # print('tableArray[1] type?', type(tableArray[1]))  # list
    # print('tableArray[1] length?', len(tableArray[1]))  # 1
    # def load_data():
    #     return pd.DataFrame(
    #         {
    #             tableData[0][0]: [tableData[1][1]],
    #             "second column": [10, 20, 30, 40],
    #         }
    #     )
    # # Boolean to resize the dataframe, stored as a session state variable
    # st.checkbox("Use container width", value=False, key="use_container_width")
    # df = load_data()
    # # Display the dataframe and allow the user to stretch the dataframe
    # # across the full width of the container, based on the checkbox value
    # st.dataframe(df, use_container_width=st.session_state.use_container_width)

except error.HTTPError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
except error.URLError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
