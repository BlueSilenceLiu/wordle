from main import dw, RawSolver, choice

class Solver:
    def __init__(self, word_set=dw, outputs="CEN"):
        self.rsv = RawSolver(word_set, outputs)
        self.full_set = word_set

    def inp(self, res, word):
        self.rsv.inp(res, word)

    def get(self):
        if self.rsv.available == self.full_set:
            return "adieu"
        else:
            return choice(self.rsv.get())


