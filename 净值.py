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
    data = ak.stock_index_pb_lg()
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data/净值.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()

if __name__ == '__main__':
    doExec()
