from PerformanceAnalytics import returns
from pandas.util.testing import assert_frame_equal, assert_almost_equal
import pandas as pd
import numpy as np

class TestReturns:
    def test_annualized(self):
        dates = pd.date_range("1/1/2010", periods=12, freq="M")
        df = pd.DataFrame([0.1 for i in range(12)], index=dates)
        assert_almost_equal(returns.annualized(df), 2.138428)
        
    def test_cumulative(self):
        pass
    
    def test_calculate(self):
        dates = pd.date_range("1/1/2010", periods=12, freq="M")
        prices = pd.DataFrame([i for i in range(1, 13)], index=dates)
        rets = returns.calculate(prices)
        ans = pd.DataFrame([float(i+1)/i - 1 for i in range(1, 13)], index=dates).shift(1)
        assert_frame_equal(rets, ans)
        
        rets = returns.calculate(prices, "log")
        ans = pd.DataFrame([np.nan, 0.69314718, 0.40546511, 0.28768207, 0.22314355, 
                           0.18232156, 0.15415068, 0.13353139, 0.11778304, 
                           0.10536052, 0.09531018, 0.08701138], index=dates)
        assert_frame_equal(rets, ans)
        
    def test_geltner(self):
        dates = pd.date_range("1/1/2010", periods=5, freq="M")
        df = pd.DataFrame([i for i in range(5)], index=dates)
        df = returns.geltner(df)
        ans = pd.DataFrame([np.nan, 1.666667, 2.666667, 3.666667, 4.666667], index=dates)
        assert_frame_equal(df, ans)
        
    def test_relative(self):
        dates = pd.date_range("1/1/2010", periods=5, freq="M")
        Ra = pd.DataFrame([0.1*i for i in range(1, 6)], index=dates)
        Rb = pd.DataFrame([0.1 for i in range(1, 6)], index=dates)
        relative_rets = returns.relative(Ra, Rb)
        ans = pd.DataFrame([1.000000, 1.090909, 1.289256, 1.640872, 2.237552], index=dates,
                           columns = ["0/benchmark"])
        assert_frame_equal(relative_rets, ans)
        
        #Test for when Rb is a time series
        Rb = pd.TimeSeries([0.1 for i in range(1, 6)], index=dates)
        relative_rets = returns.relative(Ra, Rb)
        assert_frame_equal(relative_rets, ans)        
    