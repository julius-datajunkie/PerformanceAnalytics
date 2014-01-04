import statsmodel


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
    Calculates returns by removing estimating or liquidity bias in real estate index returns
    It has since been appleid with success to other return series that show autocorrelation or illiquidity
    """
    pass


def rebalancing(R, weights):
    """
    Calculates weighted returns for a portfolio of assets. This function is used
    when you have a portfolio that is periodically rebalanced, and multiple time
    periods with different weights. This function will subset the return series to
    only include returns for assets for which weight is provided.
    R: pandas dataframe/timeseries of asset returns
    weights:
    """


