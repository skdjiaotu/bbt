import pandas as pd
import akshare as ak
import datetime
import time
import math

from common import databaseSession
from models import stock_models
from models.stock_models import ConsecutiveStock


# 列名与数据对其显示

def doExec():
    data = ak.stock_rank_cxfl_ths()
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data/持续放量.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()
    sourceSession = databaseSession.createSession("sourceDatabase")
    # for index, row in df.iterrows():
    #     consecutiveStock = ConsecutiveStock(symbol=row['股票代码'],
    #                                         name=row['股票简称'],
    #                                         close=row['收盘价'],
    #                                         high=row['最高价'],
    #                                         low=row['最低价'],
    #                                         consecutive_days=row['连涨天数'],
    #                                         consecutive_momentum=row['连续涨跌幅'],
    #                                         cumulative_turnover_rate=row['累计换手率'],
    #                                         industry=row['所属行业'],
    #                                         date=datetime.date.today())
    #     sourceSession.add(consecutiveStock)
    #     sourceSession.commit()


if __name__ == '__main__':
    doExec()
