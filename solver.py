from main import dw, RawSolver
from entropy import ged

class Solver:
    def __init__(self, word_set=dw, outputs="CEN", entropy_file_location="default_words.entropy"):
        self.rsv = RawSolver(word_set, outputs)
        self.full_set = word_set
        self.ent = ged(entropy_file_location)

    def inp(self, res, word):
        self.rsv.inp(res, word)

    def get(self):
        unavailable = []
        for w in self.ent.keys():
            if w not in self.rsv.available:
                unavailable.append(w)
        for w in unavailable:
            del self.ent[w]
        return max(zip(self.ent.values(), self.ent.keys()))[1]
