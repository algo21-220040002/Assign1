
import pandas as pd
import numpy as np

class Markowitz_model:
    """Markowitz_model
    Use Markowitz model to do the asset allovation and portfolio management.
    """

    def __init__(self,
                 df_ER:pd.DataFrame,
                 covMat:np.ndarray,
                 rf:float,
                 z:float):
        """
        :Parameter
        :param df_ER(pd.DataFrame):The dataframe of expected return,the index is "Expected_Return",the columns are the name of assets.
        :param covMat(np.ndarray): The covariance of the return.
        :param rf：risk free rate.
        :param z(float):objective return
        """
        self.df_ER=df_ER
        self.rf=rf
        self.covMat=covMat
        self.z=z

    def portfolio(self)->tuple:
        """
        Calculate the optimized portfolio of the assets.
        :returns
        :return w0(float):It's the weight of the risk free asset in the portfolio.
        :return w(matrix):It's the matrix of the weight of the risky assets.
        """
        num=len(self.df_ER.columns)  #the num of assets
        eta=np.mat(np.ones((num,1)))
        Expected_excess_return=np.mat(self.df_ER.values.T-self.rf/12)

        C_inv=np.mat(self.covMat).I  #The invese matrix of the covariance matrix
        wp=(1/((eta.T*C_inv*Expected_excess_return)[0,0]))*C_inv*Expected_excess_return
        # w0=1-(self.z-self.rf/12)/((wp.T*Expected_excess_return)[0,0])
        # w=(1-w0)*wp
        portfolio={}
        for i in range(len(self.df_ER.columns)):
            asset=self.df_ER.columns[i]
            portfolio[asset]=wp[i,0]
        return portfolio





