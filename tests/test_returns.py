from PerformanceAnalytics import returns
import pandas as pd


class TestReturns:
    def test_annualized(self):
        dates = pd.date_range("1/1/2010", periods=12, freq="M")
        df = pd.DataFrame([0.1 for i in range(12)], index=dates)
        assert abs(returns.annualized(df) - 2.138428) < 0.0001
