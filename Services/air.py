from csv import reader
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_pollution():
    try:
        limassolGeo = {"lat": '33.0413', "lon": '33.0413'}
        # X-RapidAPI-Key = '082903c5a0msh3be58c7cee21399p1fa84ejsn1d942a71efcc'
        # X-RapidAPI-Host = 'air-quality.p.rapidapi.com'
        #
        # result_bytes = request.urlopen(
        #     "http://api.airvisual.com/v2/nearest_city?key=cb5750e6-34fb-4cf3-b605-a497c44112ce").read(
        #
        # ).decode(
        #     'UTF-8')
        # TODO: check bookmarks to add headers to api call
        result_bytes = request.urlopen(
            " https://api.ambeedata.com/latest/by-lat-lng?lat=33.0413&lng=33.0413").read(

        ).decode(
            'UTF-8')
        print('result_bytes', result_bytes)
        return []

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
