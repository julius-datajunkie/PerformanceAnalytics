import numpy as np
import returns
import math
from frequency import Frequency


def periodicity(df):
    """
    Frequencies higher than daily will not be available
    """
    med = np.median(np.diff(df.index.values))
    seconds = int(med.astype('timedelta64[s]').item().total_seconds())
    freq = Frequency()
    if seconds < 60:
        freq.label = "S"
        freq.scale = None
    elif seconds < 3600:
        freq.label = "T"
        freq.scale = None
    elif seconds < 86400:
        freq.label = "H"
        freq.scale = None
    elif seconds == 86400:
        freq.label = "D"
        freq.scale = 252
    elif seconds <= 604800:
        freq.label = "W"
        freq.scale = 52
    elif seconds <= 2678400:
        freq.label = "M"
        freq.scale = 12
    elif seconds <= 7948800:
        freq.label = "Q"
        freq.scale = 4
    else:  # anything lower than year is deemed as yearly
        freq.label = "A"
        freq.scale = 1
    return freq

def set_alpha_prob(p):
    if p >= 0.51:
        alpha = 1 - p
    else:
        alpha = p
    return alpha

def centered_moment(R, power):
    return returns.centered(R).pow(power).mean()

def M3_MM(R, mu=None):
    """
    http://www.quantatrisk.com/2013/01/20/coskewness-and-cokurtosis/
    Assume equal weighted assets in the portfolio
    """
    cAssets = len(R.columns)
    T = len(R)
    if mu is None:
        mu = R.mean()
    M3 = np.zeros((cAssets, cAssets**2))
    z = R - R.mean()
    for i in range(T):
        row = z.ix[i,:]
        row.shape = (cAssets, 1)
        M3 = M3 + np.kron(np.outer(row, row.T), row.T)
    return 1.0/T * M3

def M4_MM(R, mu=None):
    """
    http://www.quantatrisk.com/2013/01/20/coskewness-and-cokurtosis/
    Assume equal weighted assets in the portfolio
    """
    cAssets = len(R.columns)
    T = len(R)
    if mu is None:
        mu = R.mean()
    M4 = np.zeros((cAssets, cAssets**3))
    z = R - R.mean()
    for i in range(T):
        row = z.ix[i,:]
        row.shape = (cAssets, 1)
        M4 = M4 + np.kron(np.kron(np.outer(row, row.T), row.T), row.T)
    return 1.0/T * M4