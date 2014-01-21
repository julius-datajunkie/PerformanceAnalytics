import utils
import numpy as np
import scipy.stats as stats


def Gaussian(R, p):
	alpha = utils.set_alpha_prob(p)
	m2 = utils.centered_moment(R, 2)
	VaR = -R.mean() - stats.norm.ppf(alpha) * np.sqrt(m2)
	return VaR