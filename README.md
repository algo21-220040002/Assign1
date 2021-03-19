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


