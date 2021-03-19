import pandas as pd
import numpy as np

class ER_EC:
    """ER_EC
    It's used to calculate the expected return and expected covariance.
    """
    def __init__(self,
                 df:pd.DataFrame):
        """
        :parameter
        :param df(pd.DataFrame):The dataframe includes the net_value of the assets,the index is the datetime, and the columns are the name or code of the assets.
        """
        self.df=df
        self.assets=df.columns.tolist()

    def ER(self)->pd.DataFrame:
        """
        :returns
        :return data(pd.DataFrame):It's the expected rate of return of the assets.The index is 'Expected_Return',the
        :return columns are the name of assets.
        """
        df=self.df.copy()
        # df=df.resample('M').last()
        data = pd.DataFrame(index=['Expected_Return'],columns=self.assets)
        for asset in self.assets:
            df[asset+'return']=df[asset].pct_change()
            data.loc['Expected_Return',asset]=df[asset+'return'].mean()
        return data

    def EC(self)->pd.DataFrame:
        """
        :returns
        :return data(pd.DataFrame):A dataframe that consists of the covariance matrix.
        """
        df=self.df.copy()
        # df = df.resample('M').last()
        for asset in self.assets:
            df[asset + 'return'] = df[asset].pct_change()
        df=df.drop(self.assets, axis=1)
        df=df.dropna(axis=0,how='any')
        m=np.array(df)
        covMat=np.cov(m,rowvar=False)
        data=pd.DataFrame(covMat)
        return data


    def er_ec(self):
        """
        Store the data into the disk.
        """
        df1=ER_EC.ER(self)
        df2=ER_EC.EC(self)
        return df1,df2




