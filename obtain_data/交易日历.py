import pandas as pd
import akshare as ak

def doExec():
    tradeData = ak.tool_trade_date_hist_sina()
    writer = pd.ExcelWriter('../data/交易日历.xlsx')
    tradeData.tail(1000).to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()
    print()
    exit()


if __name__ == '__main__':
    doExec()
