import pandas as pd
import numpy as np
import math
import utils


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


def excess(R, Rf=0):
    """
    Calculates the returns of an asset in excess of the given "risk free rate"
    for the period
    R: pandas dataframe, timeseries
    Rf: risk free rate can be a timeseries or a number
    """
    return R - Rf


def Geltner(R):
    """
    Calculates returns by removing estimating or liquidity bias in
    real estate index returns. It has since been applied with success
    to other return series that show autocorrelation or illiquidity.
    """
    pass


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
