
import pandas as pd
import numpy as np
import datetime
from ER_EC.ER_EC import ER_EC
from Portfolio_optimization.Markowitz import Markowitz_model
from Exchange.Exchange import Exchange
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def main():
    PNL=pd.DataFrame()  #储存每期账户余额
    data=pd.read_excel(r'./data/Price_info/Price_info.xlsx',index_col=0)  #读取各资产价格信息
    data = data.resample('M').last()  #转换为月度
    assets=data.columns.tolist()  #资产列表
    exchange=Exchange(data,assets,"2021314",True)  #调取交易所
    df_price_info=pd.DataFrame()  #将从交易所获取的价格信息放进此dataframe

    fig = plt.figure(figsize=(5, 3))  #动态展示出账户余额金额变化
    plt.ion()

    for date in data.index[:-8]: #按照每月月末日期进行回测
        df_price_info=pd.concat([df_price_info,exchange.get_price_info(date)],axis=0)
        if len(df_price_info)>10:  #当搜集交易所交易数据超过10个月
            er_ec = ER_EC(df_price_info[-10:])
            df1,df2=er_ec.er_ec()
            covMat = df2.values
            markowitz_model = Markowitz_model(df1, covMat, 0, 0.000001)  #用马科维兹模型进行优化
            portfolio= markowitz_model.portfolio()
            print('日期是:',date)
            account_info=exchange.get_account_info(date)
            strtegy={}
            for asset in assets:
                strtegy[asset]=account_info['total_banlance']*portfolio[asset]
            exchange.trade(strtegy,date)
            PNL.loc[date,'PNL']=exchange.get_account_info(date)['total_banlance']
            print('账户信息是')
            print(exchange.get_account_info(date))
            if len(PNL)>=2:
                xs=[PNL.index[-2],date]
                ys=[PNL.loc[PNL.index[-2],'PNL'],PNL.loc[date,'PNL']]
                plt.plot(xs, ys)
                plt.pause(1)
if __name__=="__main__":
    main()