from random import choice
from load import dw

class Wordle:
    def __init__(self, ans=None, mxt=6, outputs="CEN"):
        if ans is None:
            self.ans = choice(dw)
        else:
            self.ans = ans
        self.mxt = mxt
        self.t = 1
        self.outputs = outputs

    def inp(self, inp):
        self.t += 1
        if self.t <= self.mxt+1:
            out = ""
            for i in range(len(self.ans)):
                if inp[i] == self.ans[i]:
                    out += self.outputs[0]
                elif inp[i] in self.ans:
                    out += self.outputs[1]
                else:
                    out += self.outputs[2]
            if inp == self.ans:
                return 1
            else:
                return out
        else:
            return 0

class RawSolver:
    def __init__(self, word_set=dw, outputs="CEN"):
        self.outputs = outputs
        self.available = word_set.copy()

    def inp(self, res, word):
        unavailable_indexes = []
        for i in range(len(self.available)):
            cur = self.available[i]
            if Wordle(cur).inp(word) != res:
                unavailable_indexes.append(i)
        unavailable_indexes.reverse()
        for index in unavailable_indexes:
            del self.available[index]
        return self

    def get(self):
        return self.available
