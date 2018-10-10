

class Classification:
    label: str
    conf: float
    tl: (float, float)
    br: (float, float)

    def __init__(self, clf: dict):
        self.label = clf["label"]
        self.conf = clf["confidence"]
        self.tl = clf["topleft"]
        self.br = clf["bottomright"]

    def __eq__(self, other):
        """
            Checks if a different classification is equal to the classification of what this function is called on.

            Parameters
            ----------
            other : Classification
                Different classification to what this function is being called on.

            Returns
            -------
                True if classes match, False if not.
        """
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        out = "Label: " + self.label + " Confidence: " + str(self.conf) + " Top Left " + str(self.tl) + \
              " Bottom Right: " + str(self.br)
        return out
