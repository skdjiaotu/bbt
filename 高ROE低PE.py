import pandas as pd
import akshare as ak
import datetime
import time
import math


# 市净率 PB：总市值/净资产
# 市盈率 PE：总市值/净利润
# 第一个公式， ROE=净利润/净资产 ，这公式就是ROE的定义，非常直观。根据用途，ROE还可以细分为：一种是全面摊薄ROE，ROE=净利润/期末净资产；另一种是加权ROE，ROE=净利润/（期初和期末净资产的平均值）
# 经营者喜欢摊薄ROE，投资者喜欢加权ROE。在净利润与净资产数额较为可靠的情况下，一般而言，ROE处于10%-15%，为一般公司；ROE处于15%-20%，为优秀公司；ROE处于20%-30%，为杰出公司
# 第二个公式，ROE=（净利润/股票总数)/(净资产/股票总数)=每股收益(E)/每股净资产(A)，这公式说明了ROE与每股收益、每股净资产之间的关系。从中可以看出，提高ROE有五条途径：
# 1.E提高，A提高，财务状况最好，值得褒奖；
# 2.E提高，A不变，财务状况良好，值得提倡；
# 3.E提高，A下降，财务状况不明，需要查明；
# 4.E不变，A下降，财务状况有问题，应予警惕；
# 5.E下降，A下降，财务状况糟糕，须摒弃
# 第三个公式，ROE=净利润/净资产＝（PB：总市值/净资产）/（PE：总市值/净利润）=PB/PE。PE反映的是预期溢价，PB反映的是资产溢价。这个公式说明ROE与PB和PE的制约关系，如一只股票ROE特别高，那么PB就会相对较大，PE相对较小。
# 第四个公式，ROE=①净利率×②总资产周转率×③权益乘数（杠杆率），这也是杜邦分析公式。其中权益乘数=1/（1-资产负债率）。因此，一家企业可以通过提高净利率、总资产周转率和资产负债率来提高ROE。
# ①净利润率反映公司赚钱能力，①↑代表产品利润高，赚钱能力强，也说明管理层的管理能力良好，能让产品保持持续的竞争力。
# ②总资产周转率衡量企业的资产运营效率的高低。①↑+②↑说明产品能够高效生产、销售并且产品利润率高（高效+多钱）。提高净利率和资产周转率这两种方法，是企业通过挖掘自身潜力来提高ROE。
# ③杠杆率反映公司负债程度的高低，权益乘数（杠杆率）=1/（1-资产负债率）。杠杆率越高，证明公司运用外部资金能力越强，①↑+②↑+③↑=用别人的钱为自己公司高效生产利润率高的产品（高效+多钱+杠杆）。不过，企业的杠杆水平高，结果是挣得多了，但风险也随之加大

def doExec():
    stock_individual_info_em_df = ak.stock_individual_info_em(symbol="000001")
    print(stock_individual_info_em_df)
    dividendArray = []
    failureArray = []
    data = ak.stock_financial_abstract(symbol='000001')
    # data = ak.stock_financial_analysis_indicator(symbol='000001',start_year="2020")
    print(data)
    exit()
    file_path = r'./data/stock.xlsx'
    df = pd.read_excel(file_path, sheet_name="Sheet1", dtype=str)
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
