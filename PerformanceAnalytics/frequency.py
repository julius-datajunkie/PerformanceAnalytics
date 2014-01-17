class Frequency:
    def __init__(self, scale=None, label=None):
        self.label = label
        self.scale = scale

    def __str__(self):
        return self.label
