import pandas as pd
import akshare as ak

def doExec():
    # 涨停
    # data = ak.stock_zt_pool_em(date="20240528")
    # print(data)
    #
    data = ak.stock_zt_pool_em(date="20241016")
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data/涨停板.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()


if __name__ == '__main__':
    doExec()
