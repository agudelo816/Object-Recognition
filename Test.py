
class Test:

    def __init__(self, type, variation):
        self.type = type
        self.variation = variation
        self.queries = 0
        self.score = 0

    def add_score(self, increment):
        self.score += increment
        self.queries += 1

    def get_mean(self):
        return self.score/self.queries


