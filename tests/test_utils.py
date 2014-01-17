import pandas as pd
from PerformanceAnalytics import utils


def test_utils():
    dates = pd.date_range('1/1/2010', periods=12, freq="M")
    df = pd.DataFrame([0 for i in range(12)], index=dates)
    freq = utils.periodicity(df)
    assert freq.scale == 12
    assert freq.label == "M"
