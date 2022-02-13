from load import dw
from main import Wordle
from math import log2
from os import remove
from load import lcw


def entropy(word, word_set=dw):
    res_dict = {}
    for _word in word_set:
        res = Wordle(_word).inp(word)
        if res != 1:
            try:
                res_dict[res] += 1
            except KeyError:
                res_dict[res] = 1
    return float(sum([log2(len(word_set)/i)*i/len(word_set) for i in res_dict.values()]))

def reload_entropy(path="default_words.txt", log=False):
    word_set = lcw(path)
    entropies = {}
    for i in range(len(word_set)):
        entropies[entropy(word_set[i], word_set)] = word_set[i]
        if log:
            print(f"{i+1}/{len(word_set)}")

    res = "\n".join([entropies[i] + "\t" + str(i) for i in sorted(entropies.keys(), reverse=True)])
    try:
        remove(path[:-4]+".entropy")
    except FileNotFoundError:
        pass
    finally:
        with open(path[:-4]+".entropy", 'x') as entropy_file:
            entropy_file.write(res)

if __name__ == '__main__':
    reload_entropy("usr/words.txt", log=True)
