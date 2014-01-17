import numpy as np
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
