import pandas as pd
import returns
import VaR


def VaR(R, p=0.95, method="modified", clean=None,
        portfolio_method="single", weights=None,
        mu=None, sigma=None, m3=None, m4=None, invert=True):
    """
    Calculates Value-at-Risk(VaR) for univariate, component, and marginal cases
    using a variety of analytical methods.
    """
    nrow = len(R)
    ncol = len(R.columns)
    if weights is None and portfolio_method != "single":
        print "No weights passed in, assuming equal weighted portfolio"
        weights = pd.DataFrame([1/nrow for i in range(nrow)])
    if R is not None:
        if weights is not None and portfolio_method != "single":
            if len(weights) != ncol:
                raise Exception("Number of items in weights not equal to number of columns in R")
        if clean is not None and mu is None:
            R = returns.clean(R, method=clean)
        if portfolio_method != "single":
            if mu is None:
                mu = R.mean()
            if sigma is None:
                R.cov()
            if method == "modified":
                if m3 is None:
                    m3 = M3.MM(R)
                if m4 is None:
                    m4 = M4.MM(R)
    else:
        if mu is None:
            raise Exception("Nothing to do! You must pass either R or the moments mu, sigma, etc.")
        if len(weights) != nrow:
            raise Exception("Number of items in weights not equal to number of items in the mean vector")
    if portfolio_method == "single":
        if weights is None:
            if method == "modified":
                rVaR = VaR.CornishFisher(R=R, p=p)
            elif method == "gaussian":
                rVaR = VaR.Gaussian(R=R,p=p)
            elif method == "historical":
                rVaR = -1 * R.quantile(q=1-p, 0)
            elif method == "kernel":
                raise Exception("No kernel method defined for non-component VaR")
        else:
            if method == "modified":
                rVaR = mVaR.MM(w=weights, mu=mu, sigma=sigma, M3=m3, M4=m4, p=p)
            elif method == "gaussian":
                rVaR = GVaR.MM(w=weights, mu=mu, sigma=sigma, p=p)
            elif method == "historical":
                rVaR = VaR.historical(R=R, p=p).dot(weights)
    elif portfolio_method == "component":
        if method == "modifed":
            return VaR.CornishFisher.portfolio(p, weights, mu, sigma, m3, m4)
        elif method == "gaussian":
            return VaR.Gaussian.portfolio(p, weights, mu, sigma)
        elif method == "historical":
            return VaR.historical.portfolio(R, p, weights)
        elif method == "kernel":
            return VaR.kernel.portfolio(R, p, weights)
    elif portfolio_method == "marginal":
        return VaR.Marginal(R, p, method, weights)

    return rVaR

