import sys
from urllib import request
from urllib import error


def get_factorial(number):
    try:
        numberStr = str(number)

        url_string = "https://cei521athinodoros.azurewebsites.net/api/Factorial?code" \
                     "=IIYnusOyA4Q8yqKr0jFpylLYW0t_vvQv87aB5nU18LsIAzFunUMmqQ==&number=" + numberStr
        result = request.urlopen(url_string).read().decode('UTF-8')

        return result

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
