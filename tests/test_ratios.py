from PerformanceAnalytics import ratios
import pandas as pd


class TestRatios:
    def test_kelly_ratio(self):
        pass

    def test_sharp_ratio(self):
        dates = pd.date_range("1/1/2010", periods=12, freq="M")
        # When there is no variation in returns
        df = pd.DataFrame([0.1 for i in range(12)], index=dates)
        assert ratios.sharp_ratio(df) == float('Inf')
        # Forever increasing returns
        df = pd.DataFrame([0.1 * (i + 1) for i in range(12)], index=dates)
        assert abs(ratios.sharp_ratio(df) - 1.802776) < 0.001
        # Forever decreasing returns
        df = pd.DataFrame([-0.1 * (i + 1) for i in range(12)], index=dates)
        assert abs(ratios.sharp_ratio(df) + 1.802776) < 0.001
        # Mixed returns with mean 0
        df = pd.DataFrame([-0.1 * (i + 1) for i in range(6)]
                          .extend([0.1 * (i + 1) for i in range(6)]), index=dates)
        assert abs(ratios.sharp_ratio(df)) < 0.001
        # Mixed returns with mean != 0
        df = pd.DataFrame([-0.1 * (i + 1) for i in range(7)]
                          .extend([0.1 * (i + 1) for i in range(5)]), index=dates)
        assert abs(ratios.sharp_ratio(df) + 0.2671278) < 0.001
