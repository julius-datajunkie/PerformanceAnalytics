class frequency:
    second = 0
    minutely = 1
    hourly = 2
    weekly = 3
    monthly = 4
    quarterly = 5
    yearly = 6

    def to_str(self, d):
        if d is frequency.second:
            name = "S"
        if d is frequency.minutely:
            name = "T"
        if d is frequency.hourly:
            name = "H"
        if d is frequency.weekly:
            name = "W"
        if d is frequency.monthly:
            name = "M"
        if d is frequency.quarterly:
            name = "Q"
        if d is frequency.yearly:
            name = "A"
        return name
