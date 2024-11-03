import datetime

import pandas as pd
import akshare as ak


def getTradeCal():
    pass


def isCanTradeDay(date):
    # 写入表格
    stackDay = pd.read_excel('../data/交易日历.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    dateStr = date.strftime("%Y-%m-%d")
    stackDayList = stackDay['trade_date'].dt.strftime("%Y-%m-%d")
    stackDayList = stackDayList.to_list()
    if dateStr in stackDayList:
        return True
    else:
        return False


def isCanTradeDayStr(dateStr):
    # 写入表格
    stackDay = pd.read_excel('../data/交易日历.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    stackDayList = stackDay['trade_date'].dt.strftime("%Y-%m-%d")
    stackDayList = stackDayList.to_list()
    if dateStr in stackDayList:
        return True
    else:
        return False

def getBeforeTradeDayStr():
    # 写入表格
    stackDay = pd.read_excel('../data/交易日历.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
    stackDayList = stackDay['trade_date'].dt.strftime("%Y-%m-%d")
    stackDayList = stackDayList.to_list()
    stackDayList.reverse()
    dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
    for day in stackDayList:
        if day < dateStr:
            return day

    return