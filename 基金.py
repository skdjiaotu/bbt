import pandas as pd
import akshare as ak
import datetime
import time
import math

def doExec():
    # 涨停
    # data = ak.stock_zt_pool_em(date="20240528")
    # print(data)
    #
    data = ak.fund_etf_category_sina(symbol="ETF基金")
    print(data)

    # # 300007
    # for index, row in df.iterrows():
    #     print(index)
    #     try:
    #         stockStr = row['label'] + row['A股代码']
    #         beforeDatetime = datetime.timedelta(days=5)
    #         nowDatetime = datetime.datetime.now()
    #         endDatetime = (nowDatetime - beforeDatetime).strftime("%Y%m%d")
    #         startDatetime = nowDatetime.strftime("%Y%m%d")
    #         stockData = ak.stock_zh_a_daily(symbol=stockStr, start_date=endDatetime, end_date=startDatetime)
    #         data = ak.stock_history_dividend_detail(symbol=row['A股代码'])
    #         firstDividend = data[0:1]
    #         date = datetime.date(2024, 5, 27)
    #
    #         if firstDividend['公告日期'].iloc[0] > date and firstDividend['派息'].iloc[0] > 0:
    #             newRow = firstDividend.iloc[0]
    #             print(newRow)
    #             newRow['A股代码'] = row['A股代码']
    #             newRow['A股简称'] = row['A股简称']
    #             newRow['最近收盘价'] = stockData.head(1).iloc[0]['close']
    #             newRow['股息率'] = round(10 * firstDividend['派息'].iloc[0] / stockData.head(1).iloc[0]['close'],
    #                                      2)
    #             dividendArray.append(newRow)
    #
    #     except Exception as e:
    #         print(row)
    #         failureArray.append(row)
    #         continue
    #
    #     time.sleep(6)
    #
    # sorted(dividendArray, key=lambda x: x['派息'])
    # df = pd.DataFrame(dividendArray)
    # writer = pd.ExcelWriter('data/output2.xlsx')
    # df.to_excel(writer, sheet_name='Sheet1', index=False)
    # writer.close()
    #
    # writer = pd.ExcelWriter('data/failure.xlsx')
    # df.to_excel(writer, sheet_name='Sheet1', index=False)
    # writer.close()


if __name__ == '__main__':
    doExec()
