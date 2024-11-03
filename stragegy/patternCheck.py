import datetime

import pandas as pd
import akshare as ak
import talib

from util.tools import isCanTradeDay, getBeforeTradeDayStr


def doExec():
    now = datetime.datetime.now()
    today = now.strftime("%Y%m%d")
    eighteenBeforeDay = (now - datetime.timedelta(days=360)).strftime("%Y%m%d")

    data = ak.stock_zh_a_spot_em()
    df = pd.DataFrame(data)
    # writer = pd.ExcelWriter('../data/实时行情.xlsx')
    # df.to_excel(writer, sheet_name='Sheet1', index=False)
    # writer.close()

    for index, row in df.iterrows():
        if row["代码"] == '600150':
            checkoutPattern(row, eighteenBeforeDay, today)

    # 查找合适目标
    flag, data = checkoutPattern()
    candidate = []
    if flag:
        candidate = data

    # 写入表格
    writer = pd.ExcelWriter('../data/可以考虑.xlsx')
    candidate.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()


def checkoutPattern(data, start_date, end_date):
    historyData = getHistoryData(data["代码"], start_date, end_date)
    print(data["代码"])
    print(historyData)
    #data = talib.CDLADVANCEBLOCK(historyData['open'], historyData['high'], historyData['low'], historyData['close'])
    lineP5 = talib.SMA(historyData['close'],timeperiod=5)
    lineP20 = talib.SMA(historyData['close'],timeperiod=20)
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddsc    print(lineP20[-1])
aaaaaaaaaaaaaaaaaaad  juyj7uiiojjjfgtp;jjjjjjjjjjjjjjjjjjuyg44444r 5        r ,cddddddddddddddscc    print(lineP20[-1])
    print(type(lineP5[-1]))

    exit()



def getHistoryData(symbol, start_date, end_date):
    # 使用akshare获取数据
    df = ak.stock_zh_a_hist(symbol=symbol,
                            period="daily",
                            start_date=start_date,
                            end_date=end_date,
                            adjust="qfq")
    return df.rename(
        columns={'日期': 'date', '开盘': 'open', '收盘': 'close', '最高': 'high', '最低': 'low',
                 '成交量': 'volume', '成交价': 'amount', '振幅': 'change', '换手率': 'ratio'})


if __name__ == '__main__':
    doExec()
