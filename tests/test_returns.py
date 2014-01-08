from PerformanceAnalytics import returns
import pandas as pd


class TestReturns:
    def test_rebalancing(self):
        weights = pd.read_csv("weights.csv", parse_dates=[0])
        edhec = pd.read_csv("edhec.csv", parse_dates=[0])
        edhec.index = edhec.ix[:, 0]
        weights.index = weights.ix[:, 0]
        weights = weights.ix[:, 1:]
        edhec = edhec.ix[:, 1:]
        assert len(returns.rebalancing(edhec, weights)) == 116
