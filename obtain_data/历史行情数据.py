import pandas as pd
import akshare as ak
import mplfinance as mpf
import talib
import numpy as np


def doExec(symbol="600811"):
    # 使用akshare获取数据
    df = ak.stock_zh_a_hist(symbol=symbol, period="daily", start_date="20231001", end_date='20241023', adjust="qfq")
    df = df.rename(
        columns={'日期': 'date', '开盘': 'open', '收盘': 'close', '最高': 'high', '最低': 'low',
                 '成交量': 'volume', '成交价': 'amount', '振幅': 'change', '换手率': 'ratio'})

    # stock_individual_info_em_df = ak.stock_individual_info_em(symbol=symbol)

    # 设置mplfinance的蜡烛颜色，up为阳线颜色，down为阴线颜色
    my_color = mpf.make_marketcolors(up='r',
                                     down='g',
                                     edge='inherit',
                                     wick='inherit',
                                     volume='inherit')
    # 设置图表的背景色
    my_style = mpf.make_mpf_style(marketcolors=my_color,
                                  figcolor='(0.82, 0.83, 0.85)',
                                  gridcolor='(0.82, 0.83, 0.85)')

    fig = mpf.figure(style='yahoo', figsize=(10.8, 6.4))
    ax1 = fig.add_subplot(2, 2, 1)
    # fig.text(0.14, 0.89, f'{np.round(last_data["open"], 3)} / {np.round(last_data["close"], 3)}')
    # fig.text(0.14, 0.86, f'{last_data["change"]}')
    # fig.text(0.22, 0.86, f'[{np.round(last_data["pct_change"], 2)}%]')
    # fig.text(0.12, 0.86, f'{last_data.name.date()}')
    # fig.text(0.40, 0.90, '高: ')
    # fig.text(0.40, 0.90, f'{last_data["high"]}')
    # fig.text(0.40, 0.86, '低: ')
    # fig.text(0.40, 0.86, f'{last_data["low"]}')
    # fig.text(0.55, 0.90, '量(万手): ')
    # fig.text(0.55, 0.90, f'{np.round(last_data["volume"] / 10000, 3)}')
    # fig.text(0.55, 0.86, '额(亿元): ')
    # fig.text(0.55, 0.86, f'{last_data["value"]}')
    # fig.text(0.70, 0.90, '涨停: ')
    # fig.text(0.70, 0.90, f'{last_data["upper_lim"]}')
    # fig.text(0.70, 0.86, '跌停: ')
    # fig.text(0.70, 0.86, f'{last_data["lower_lim"]}')
    # fig.text(0.85, 0.90, '均价: ')
    # fig.text(0.85, 0.90, f'{np.round(last_data["average"], 3)}')
    # fig.text(0.85, 0.86, '昨收: ')
    # fig.text(0.85, 0.86, f'{last_data["last_close"]}')

    # 行索引必须是pandas.DatetimeIndex
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index(['date'], drop=True)

    #
    # fig = mpf.figure(style='charles', figsize=(7, 8))
    # ax1 = fig.add_subplot(2, 1, 1)
    # ax2 = fig.add_subplot(3, 1, 3)
    # 通过ax=ax1参数指定把新的线条添加到ax1中，与K线图重叠
    # 求5日均线
    ma10 = talib.SMA(df['close'], timeperiod=10)
    ma30 = talib.SMA(df['close'], timeperiod=30)
    ma60 = talib.SMA(df['close'], timeperiod=60)
    ma200 = talib.SMA(df['close'], timeperiod=200)

    # 计算MACD
    # macd: 差离值
    # signal: 信号线
    # macdhist: MACD柱状图值
    macd, signal, macdHist = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)

    redHist = np.where(macdHist > 0, macdHist, 0)
    greenHist = np.where(macdHist < 0, macdHist, 0)

    # 添加多条均线
    ap = [mpf.make_addplot(ma10, color='r'),
          mpf.make_addplot(ma30, color='b'),
          mpf.make_addplot(ma60, color='c'),
          mpf.make_addplot(ma200, color='y'),
          mpf.make_addplot(macd, color='y', panel=2, label="差离值DIF"),
          mpf.make_addplot(signal, color='b', panel=2, label="讯号线DEA"),
          mpf.make_addplot(redHist, color='r', panel=3, type='bar'),
          mpf.make_addplot(greenHist, color='g', panel=3, type='bar'),
          ]

    mpf.plot(df, volume=True,
             scale_width_adjustment=dict(volume=0.5, candle=1.15, lines=0.65),
             type='candle',
             style=my_style,
             addplot=ap)

    mpf.show()


if __name__ == '__main__':
    doExec()
