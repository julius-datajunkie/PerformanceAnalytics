import returns


def kelly_ratio(R, Rf=0, method="half"):
    KR = returns.excess(R, Rf).mean() / R.var()
    if method == "half":
        KR = KR / 2
    return KR
