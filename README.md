# Portfolio Management

Portfolio management provides a tool to use Markowitz'a Mean variance model to rebanlance your portfolio every month and do a backtest.

## ER_EC

ER_EC is a package that calculate the expected return and expected covariance matrix of the assets. The expected return and expected covariance matrix is very important because it
will be used in the mean variance model.

## Portfolio_optimization

Portfolio_optimization is the part of the mean variance model and it will give the weight of different assets. Here I only use Markowitz'a Mean variance model, there are many model to do portfolio optimization after Markowitz like Black-Litterman model and so on. So i think it's very easy to incorporate other models in this system and it's scalable.

## Exchange

Exchange is a imitate of the real exchange and the backtest framework is event-driven. Here, the exchange will read the price information and send it to the trader, the trader will receive the price information month by month, and then the trader use the Porforlio_optimization to give the objective position of each asset to the eachange, then the exchange will calculate the banlance, position of the trader and store it to the 2021314.pkl. The name of the pkl is the account id of the trader.

 So it's a model of the real exchange and I hope it can imporove the efficiency of the backtest.
 
 ## Engine
 The Engine.py is the main function of the system. It will import the packages above and run the system.
 
 ## Run the system
 
 ### data
 
 I select three assets in Chinese market: They are "医药生物","传媒","新能源指数". And I do the backtest from 2018 to 2020.
 
 ### Portfolio optimization
 The Portfolio_optimization will use data of last ten months to give the objective position.
 
 The following are some of the objective portfolio the model gives:
 ![image](https://github.com/algo21-220040002/Assign1/blob/master/Paper/portfolio.jpg)
 
 The trader will send the objective position to the exchange then the exchange will update the information of the account such as the total banlance,the cash, the banlance of one asset.
 
  ### The account information in the exchange
 The followings are the account info in the exchange:
 ![image](https://github.com/algo21-220040002/Assign1/blob/master/Paper/account_info.jpg)
 

 ### The PNL
 Finally, it will draw the PNL dynamically as time goes by. The following is a examplt:
  ![image](https://github.com/algo21-220040002/Assign1/blob/master/Paper/PNL.png)
  
  
 ## Summary
 
 Through the system, it's obvious that the mean variance model is vary sensitive to the parameter and in the system I suppose that short is allowed but in Chinese market it't a liitle difficult to short so I think there will be two points that can be improved.
 
 ### To change the suppose to satisfy the condition of Chinese stock markets.
 
 ### Use other models like Black-Litterman, risk parity and so on to improve the robustness of the strategy and make it more efficiency.
 



