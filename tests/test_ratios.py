from PerformanceAnalytics import ratios
import pandas as pd


class TestRatios:
    def test_kelly_ratio(self):
        edhec = pd.read_csv("edhec.csv", parse_dates=[0])
        edhec.index = edhec.ix[:, 0]
        edhec = edhec.ix[:, 1:]
        print ratios.returns(edhec.ix[:,0])
