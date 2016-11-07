from Result import Result
class Query():
    def __init__(self, query):
        self.query = query
        self.results = []

    def add_result(self, res_obj):
        self.results.append(res_obj)

    def get_result(self, index):
        return self.results[index]



    def get_query(self):
        return self.query
