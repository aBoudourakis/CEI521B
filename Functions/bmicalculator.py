import sys
from urllib import request
from urllib import error


def get_bmi(height, weight):
    try:
        heightStr = str(height)
        weightStr = str(weight)

        url_string = "https://cei521athinodoros.azurewebsites.net/api/BMI?code=ltvyB1C9AG4tpOzPZBStxjh_zUiD-hqjXVK0KeMb0vUqAzFukhDMoQ==&height=" + heightStr + "&weight=" + weightStr
        result = request.urlopen(url_string).read().decode('UTF-8')
        print('result', result)

        return result

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
