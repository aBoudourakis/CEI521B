import sys
from urllib import request
from urllib import error

try:
    ResultBytes = request.urlopen(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Limassol?unitGroup"
        "=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv").read().decode('UTF-8')

    print('ResultBytes', ResultBytes)
    # Parse the results as CSV
    # CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
    # Parse the results as JSON
    # jsonData = json.loads(ResultBytes.decode('utf-8'))
except error.HTTPError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
except error.URLError as e:
    ErrorInfo = e.read().decode()
    print('Error code: ', e.code, ErrorInfo)
    sys.exit()
