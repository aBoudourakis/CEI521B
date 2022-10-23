import csv
import re
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
    print('array', array)
    # print('len(array[0])', len(array[0]))
    # tableArray = []
    for row in array:
        # print('row', row.split('(?:^"?|, ?"?)\K(?:(?<=").+?(?=")|[\w-]+)'))
        print('row', re.split(r'".+?"|[\w-]+', row))

    # def load_data():
    #     return pd.DataFrame(
    #         {
    #             "first column": [1, 2, 3, 4],
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
