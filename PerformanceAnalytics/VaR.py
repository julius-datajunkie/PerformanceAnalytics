import utils
import numpy as np
import scipy.stats as stats
import pandas as pd
import returns

def gaussian(R, p):
	alpha = utils.set_alpha_prob(p)
	m2 = utils.centered_moment(R, 2)
	VaR = -R.mean() - stats.norm.ppf(alpha) * np.sqrt(m2)
	return VaR

def portm2(w, sigma):
	"""
	Calculate the second moment of a portfolio
	"""
	return w.dot(sigma).dot(w)

def gaussian_portfolio(p, w, mu, sigma):
	alpha = utils.set_alpha_prob(p)
	p = alpha
	location = w.dot(mu)
	pm2 = portm2(w, sigma)
	dpm2 = derportm2(w, sigma)
	qnorm = stats.norm.ppf(alpha)
	VaR = -location -  qnorm * np.sqrt(pm2)
	derVaR = mu - qnorm * (0.5 * dpm2) / np.sqrt(pm2)
	contrib = w.dot(derVaR)
	pct_contrib = contrib / VaR
	if (abs(contrib.sum() - VaR) > 0.01 * abs(VaR)):
		raise Exception("Contribution does not add up")
	else:
		ret = 
	return ret

def var(R, p=0.95, method="modified", clean=None,
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
        weights = np.array([1/nrow for i in range(nrow)])
    	#Needs to make sure that weights has the correct dimension to do algebra
    	weights.shape = (nrow,1)
    if R is not None:
        if weights is not None and portfolio_method != "single":
            if len(weights) != ncol:
                raise Exception("Number of items in weights not equal to number of columns in R")
            weights.shape = (nrow,1)
        if clean is not None and mu is None:
            R = returns.clean(R, method=clean)
        if portfolio_method != "single":
            if mu is None:
                mu = R.mean()
            if sigma is None:
                R.cov()
            if method == "modified":
                if m3 is None:
                    m3 = utils.M3_MM(R)
                if m4 is None:
                    m4 = utils.M4_MM(R)
    else:
        if mu is None:
            raise Exception("Nothing to do! You must pass either R or the moments mu, sigma, etc.")
        if len(weights) != nrow:
            raise Exception("Number of items in weights not equal to number of items in the mean vector")
    if portfolio_method == "single":
        if weights is None:
            if method == "modified":
                rVaR = CornishFisher(R=R, p=p)
            elif method == "gaussian":
                rVaR = Gaussian(R=R,p=p)
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
            return VaR.gaussian.portfolio(p, weights, mu, sigma)
        elif method == "historical":
            return VaR.historical.portfolio(R, p, weights)
        elif method == "kernel":
            return VaR.kernel.portfolio(R, p, weights)
    elif portfolio_method == "marginal":
        return VaR.Marginal(R, p, method, weights)
    return rVaR

