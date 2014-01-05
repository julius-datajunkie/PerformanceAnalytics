import numpy as np
from frequency import frequency


def periodicity(R):
    """
    This infers the periodicity of the series based on the mean difference
    of the dates.
    R: Pandas Dataframe/Series of asset return
    """
    med = np.median(np.diff(R.index.values))
    seconds = int(med.astype('timedelta64[s]').item().total_seconds())
    if seconds < 60:
        freq = frequency.second
    elif seconds < 3600:
        freq = frequency.minutely
    elif seconds < 86400:
        freq = frequency.hourly
    elif seconds == 86400:
        freq = frequency.daily
    elif seconds <= 604800:
        freq = frequency.weekly
    elif seconds <= 2678400:
        freq = frequency.monthly
    elif seconds <= 7948800:
        freq = frequency.quarterly
    else:
        freq = frequency.yearly
    return freq
