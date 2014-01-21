import returns
#import risk
import utils as utils


def kelly_ratio(R, Rf=0, method="half"):
    KR = returns.excess(R, Rf).mean() / R.var()
    if method == "half":
        KR = KR / 2
    return KR


def sharp_ratio(R, Rf=0, p=0.95,
                Func=None,
                weights=None,
                annualized=False):
    scale = 1
    if annualized:
        scale = utils.periodicity(R).scale

    def srm(R, Rf, p, Func):
        xR = returns.excess(R, Rf)
        SRM = xR.mean() / Func
    #if annualized:
    #returns.annualized(xR)/srm(R, p, invert=False)
    pass
