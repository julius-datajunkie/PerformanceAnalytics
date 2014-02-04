import pandas as pd
import numpy as np
import math
import utils

def annualized(R, scale=None, geometric=True):
    n = len(R)
    result = 0
    if scale is None:
        scale = utils.periodicity(R).scale
    if geometric:
        result = math.pow((1 + R).prod(), scale / n) - 1
    else:
        result = R.mean() * scale
    return result

def cumulative(R, geometric=True):
    """
    This function calculates the cumulative return over a period of time.
    Can produce simple or geometric return
    R: pandas dataframe, timeseries
    geometric: default to true
    """
    if not geometric:
        return R.sum()
    else:
        return (1 + R).prod() - 1

def calculate(price, method="discrete"):
    """
    
    """
    if method == "simple" or method == "discrete":
        ret = price / price.shift(1) - 1
    elif method == "compound" or method == "log":
        ret = np.log(price).diff()
        
    return ret
              
def excess(R, Rf=0):
    """
    Calculates the returns of an asset in excess of the given "risk free rate"
    for the period
    R: pandas dataframe, timeseries
    Rf: risk free rate can be a timeseries or a number
    """
    return R - Rf

def centered(R):
    """
    Calculate the demeaned returns
    """
    return R - R.mean()

def geltner(R):
    """
    Calculates returns by removing estimating or liquidity bias in
    real estate index returns. It has since been applied with success
    to other return series that show autocorrelation or illiquidity.
    """
    f_acf = R.apply(utils.acf).iloc[1].values
    return (R - R.shift(1) * f_acf) / (1 - f_acf) 

def relative(Ra, Rb):
    """
    Calculate the ratio of the cumulative performance for two assets 
    through time.
    """
    try:
        benchmark = "benchmark"
        if Rb.name != None: #Rb is a time series
            benchmark = Rb.name
        else:
            Rb.name = benchmark # Timeseries has to have a name in order for join to work
        combined = Ra.join(Rb)
    except AttributeError:
        combined = Ra.join(Rb,rsuffix="bm")
    
    result = (combined.ix[:, :-1] + 1).cumprod() / (combined.ix[:, -1] + 1).cumprod()
    result.columns = ["{}/{}".format(col, benchmark) for col in result.columns]
    return result

def rebalancing(R, weights):
    """
    Calculates weighted returns for a portfolio of assets.
    This function is used when you have a portfolio that is periodically
    rebalanced, and multiple time periods with different weights.
    This function will subset the return series to only include returns
    for assets for which weight is provided.
    R: pandas dataframe/timeseries of asset returns
    weights: pandas timeseries of portfolio weights specifying
    rebalancing weights at different times.
    """
    weights_df = pd.DataFrame(weights)
    num_assets = len(weights_df.columns)
    # weights may have shorter length resulting in NA values
    weights_df = weights_df.reindex(R.index, method="ffill").dropna()
    #re-align return series to match the weights
    R = R.reindex(weights_df.index).ix[:, :num_assets]
    dot_product = R.dot(weights_df.T)
    portfolio_return = pd.DataFrame(
        np.diagonal(dot_product), index=dot_product.index,
        columns=['portfolio_returns']
    )
    portfolio_return.index.name = 'Date'
    return portfolio_return

