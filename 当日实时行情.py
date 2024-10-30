import datetime

import pandas as pd
import akshare as ak

from common import databaseSession
from models.stock_models import StockDay


def doExec():
    # 涨停
    # data = ak.stock_zt_pool_em(date="20240528")
    # print(data)
    #
    data = ak.stock_zh_a_spot_em()
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data/实时行情.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()
    # sourceSession = databaseSession.createSession("sourceDatabase")
    # for index, row in df.iterrows():
    #     print(row)
    #     consecutiveStock = StockDay(symbol=row['代码'],
    #                                 name=row['名称'],
    #                                 gain_fall_price_ratio=row['涨跌幅'],
    #                                 gain_fall_price=row['涨跌额'],
    #                                 trading_volume=row['成交量'],
    #                                 turnover=row['成交额'],
    #                                 price_amplitude=row['振幅'],
    #                                 open=row['今开'],
    #                                 close=row['最新价'],
    #                                 high=row['最高'],
    #                                 low=row['最低'],
    #                                 yesterday_close=row['昨收'],
    #                                 volume_ratio=row['量比'],
    #                                 turnover_rate=row['换手率'],
    #                                 forward_pe_ratio=row['市盈率-动态'],
    #                                 price_book_ratio=row['市净率'],
    #                                 market_cap=row['总市值'],
    #                                 tradable_market_cap=row['流通市值'],
    #                                 growth_rate=row['涨速'],
    #                                 five_minute_limit_price=row['5分钟涨跌'],
    #                                 sixty_days_limit_price=row['60日涨跌幅'],
    #                                 begain_year_limit_price=row['年初至今涨跌幅'],
    #                                 date=datetime.date.today())
    #     sourceSession.add(consecutiveStock)
    #     sourceSession.commit()


if __name__ == '__main__':
    doExec()
