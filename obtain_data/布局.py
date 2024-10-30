import pandas as pd
import akshare as ak
import datetime
import time
import math
import mplfinance as mpf

def doExec():
    chart_width = 0.88
    ##  图表布局规划
    fig = mpf.figure(figsize=(12, 15), facecolor=(0.82, 0.83, 0.85))
    ax1 = fig.add_axes([0.05, 0.67, 0.88, 0.20])
    ax2 = fig.add_axes([0.05, 0.57, 0.88, 0.08], sharex=ax1)
    ax3 = fig.add_axes([0.05, 0.49, 0.88, 0.06], sharex=ax1)
    ax4 = fig.add_axes([0.05, 0.41, 0.88, 0.06], sharex=ax1)
    ax5 = fig.add_axes([0.05, 0.33, 0.88, 0.06], sharex=ax1)
    ax6 = fig.add_axes([0.05, 0.25, 0.88, 0.06], sharex=ax1)
    ax7 = fig.add_axes([0.05, 0.04, 0.35, 0.16])
    ax8 = fig.add_axes([0.45, 0.04, 0.15, 0.16])
    ax9 = fig.add_axes([0.64, 0.04, 0.29, 0.16])

    mpf.plot([], volume=True,
             scale_width_adjustment=dict(volume=0.5, candle=1.15, lines=0.65),
             type='candle',
             style=my_style,
             addplot=ap)

    mpf.show()


if __name__ == '__main__':
    doExec()
