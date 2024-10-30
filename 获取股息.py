import pandas as pd
import akshare as ak
import datetime
import time
import math


# 列名与数据对其显示

def doExec():
    file_path = r'./data/stock.xlsx'
    df = pd.read_excel(file_path, sheet_name="Sheet1", dtype=str)

    dividendArray = []
    failureArray = []
    # 300007
    for index, row in df.iterrows():
        if index > 2000 and index <= 3000:
            continue
        try:
            stockStr = row['label'] + row['A股代码']
            beforeDatetime = datetime.timedelta(days=5)
            nowDatetime = datetime.datetime.now()
            endDatetime = (nowDatetime - beforeDatetime).strftime("%Y%m%d")
            startDatetime = nowDatetime.strftime("%Y%m%d")
            stockData = ak.stock_zh_a_daily(symbol=stockStr, start_date=endDatetime, end_date=startDatetime)
            data = ak.stock_history_dividend_detail(symbol=row['A股代码'])
            firstDividend = data[0:1]
            date = datetime.date(2024,5,31)

            if firstDividend['股权登记日'].iloc[0] is not pd.NaT and firstDividend['股权登记日'].iloc[0] >= date and \
                    firstDividend['派息'].iloc[0] > 0:
                newRow = firstDividend.iloc[0]
                newRow['A股代码'] = row['A股代码']
                newRow['A股简称'] = row['A股简称']
                newRow['最近收盘价'] = stockData.head(1).iloc[0]['close']
                newRow['股息率'] = round(10 * firstDividend['派息'].iloc[0] / stockData.head(1).iloc[0]['close'],
                                         2)
                print(newRow)
                dividendArray.append(newRow)

        except Exception as e:
                print("抛出异常")
                print(e)
                print(row)
                failureArray.append(row)
                continue

        time.sleep(3)

    sorted(dividendArray, key=lambda x: x['派息'])
    df = pd.DataFrame(dividendArray)
    writer = pd.ExcelWriter('data/output3000.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()

    writer = pd.ExcelWriter('data/failure.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()


if __name__ == '__main__':
    doExec()
