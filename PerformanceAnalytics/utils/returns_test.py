import returns
import pandas as pd

weights = pd.read_csv("weights.csv", parse_dates=[0])
edhec = pd.read_csv("edhec.csv", parse_dates=[0])
edhec.index = edhec.ix[:, 0]
weights.index = weights.ix[:, 0]
weights = weights.ix[:, 1:]
edhec = edhec.ix[:, 1:]
print returns.rebalancing(edhec, weights).tail()
