

class Result:

    def __init__(self, type, variation):
        self.type = type
        self.variation = variation
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def get_match(self, index):
        return self.matches[index]


