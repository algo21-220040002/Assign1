
import pandas as pd
import numpy as np
import pickle
import os
from pathlib import *


def save_obj(obj:dict, name:str):
    """
    :parameter
    :param obj:The dictionary.
    :param name:The name of the dictionary you want to store.
    """
    with open(r'./'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    """
    :parameter
    :param name:The name of dictionary.
    :return: The dictionary.
    """
    with open(r'./' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


class Exchange:
    """Exchange
    It's the class of exchange.

    """
    def __init__(self,
                 data:pd.DataFrame,
                 assets:list,
                 account_id:float,
                 if_init=True,
                 commision:float=0.00025,
                 slippage_rate:float=0.0002):
        """
        Construct the object of backtest, the parameters that we need is:the historical data,cash and commision.

        :param data:pd.DataFrame:The historical data,here we use only the close price of the asset.
        :param assets:list:The name of the assets.
        :param account:float:The account id of the trader.
        :param if_init:If you need to initialize your account info.
        :param commision:float:The commision.
        :param slippage_rate:float:The slippage rate of the trading.
        """
        self.data=data
        self.assets=assets
        self.account_id=account_id
        self.commision=commision
        self.slippage_rate=slippage_rate
        self.datelist=data.index.tolist()  #The date of the backtest period.

        if os.path.exists(str(account_id)+'.pkl')==False:
            print('you do not have an account,we will help you open the account,and the initial cash is 100000')
            print('please notice that the account id is '+str(account_id))
            dic_account={}
            dic_account['date'] = '未知'  #The date.
            dic_account['rebanlance'] = False #If it has rebanlanced the position.
            dic_account['total_banlance']=100
            dic_account['cash'] = 100
            for asset in assets:
                dic_account[asset]=0  #The value of the asset.
            save_obj(dic_account, str(account_id))
        elif if_init==True:
            print('You have initialized your account information in the exchange')
            dic_account = {}
            dic_account['date']='未知'
            dic_account['rebanlance']=False
            dic_account['total_banlance'] = 100
            dic_account['cash']=100
            for asset in assets:
                dic_account[asset] = 0  # The value of the
            save_obj(dic_account, str(account_id))
            print(dic_account)
        else:
            print('you have connected to the exchange successfully')


    def get_account_info(self,date:pd.Timestamp)->dict:
        """
        Get the information of the account.
        :return:The dic of the account.
        """
        dic_account=load_obj(str(self.account_id))
        if date!=dic_account['date']:
            dic_account['total_banlance']=0
            df_return=Exchange.get_asset_return(self,date)
            for asset in self.assets:
                dic_account[asset]+=dic_account[asset]*(df_return.loc[date,asset])
                dic_account['total_banlance']+=dic_account[asset]
            dic_account['cash']=dic_account['cash']
            dic_account['total_banlance'] += dic_account['cash']

            dic_account['date']=date
            dic_account['rebanlance']=False
        return dic_account




    def get_price_info(self,date:pd.Timestamp)->pd.DataFrame:
        """
        :param date:pd.Timestamp:The date.
        :return:The price information,the index is the date and the columns are the name of assets.
        """
        df=self.data[self.assets].loc[[date],:]
        return df

    def get_asset_return(self,date:pd.Timestamp):
        """
        :param date:pd.Timestamp:The date,the return is the return of last month.
        :return:The return of the asset last month.
        """
        df=self.data[self.assets].pct_change().loc[[date],:]
        print('涨跌幅是')
        print(df)
        return df


    def trade(self,strategy:dict,date:pd.Timestamp):
        """
        It's the trade process.
        :param strategy:dict:The key is the name of asset and the value is the objective position.
        :return:It will update the account info of the trader.
        """
        account_info=Exchange.get_account_info(self,date)
        if account_info['rebanlance']==False:
            transaction_cost=0
            dic_account={}
            dic_account['total_banlance']=0
            for asset in self.assets:
                position=strategy[asset]  #Position means the money invested.
                position_change=position-account_info[asset]  #If it's lager than 0 then the position increases.
                transaction_cost=abs(position_change*self.commision+position_change*self.slippage_rate)
                value=account_info[asset]+position_change-transaction_cost
                dic_account[asset]=value
                dic_account['total_banlance']+=value
            dic_account['cash']=account_info['total_banlance']-dic_account['total_banlance']
            dic_account['total_banlance']+=dic_account['cash']
            dic_account['date']=date
            dic_account['rebanlance']=True
            save_obj(dic_account, str(self.account_id))


def main():
    exchange=Exchange(4476)

if __name__=="__main__":
    main()





