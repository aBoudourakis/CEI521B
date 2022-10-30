import json
import sys
from urllib import request
from urllib import error
import pandas as pd


def refineList(item):
    parsedItem = json.loads(item)
    coin = parsedItem.name
    symbol = parsedItem.symbol
    price = parsedItem.price
    priceChange1h = parsedItem.priceChange1h
    priceChange1d = parsedItem.priceChange1d
    priceChange1w = parsedItem.priceChange1w
    # print({coin: coin, symbol: symbol, price: price, priceChange1h: priceChange1h, priceChange1d: priceChange1d,
    #        priceChange1w: priceChange1w})
    return {coin: coin, symbol: symbol, price: price, priceChange1h: priceChange1h, priceChange1d: priceChange1d,
            priceChange1w: priceChange1w}


def get_crypto():
    try:
        ResultBytes = request.urlopen(
            "https://api.coinstats.app/public/v1/coins?skip=0&limit=5&currency=EUR").read().decode('UTF-8')
        # print('ResultBytes', ResultBytes)
        array = ResultBytes.splitlines()
        print(array)
        parsedTest = json.loads(array[0])
        print(parsedTest)
        print(type(parsedTest))
        testPdDf = pd.DataFrame.from_dict(parsedTest)
        print(testPdDf)
        print('=================')
        print(testPdDf.iloc[0])
        itemTest = testPdDf.iloc[0]
        # next line works and extracts id value
        # TODO look further into constructing desired table like weather service
        print(itemTest[0]["id"])
        print(testPdDf.iloc[1])
        # print(testPdDf.iloc[0]["name"])
        # print(type(testPdDf.iloc[0]))
        # df = pd.DataFrame(testPdDf, columns=['0', '1'])
        # print(df)
        # refinedArray = map(refineList, array) print(refinedArray) boxes = {'Color': ['Green', 'Green', 'Green',
        # 'Blue', 'Blue', 'Red', 'Red', 'Red'], 'Shape': ['Rectangle', 'Rectangle', 'Square', 'Rectangle', 'Square',
        # 'Square', 'Square', 'Rectangle'], 'Price': [10, 15, 5, 5, 10, 15, 15, 5] }
        #
        # df = pd.DataFrame(boxes, columns=['Color', 'Shape', 'Price'])
        #
        # select_price = df.loc[df['Price'] >= 10]
        # print(select_price)
        return []

    except error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except error.URLError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()


dfResult = get_crypto()
print(dfResult)
