from load import *
from random import choice
from main import Wordle


def main(max_guess_times=6, word_set=dw, outputs="CEN"):
    global out
    game_index = 0
    while True:
        game_index += 1
        print("********** Game No.{} **********".format(game_index))
        ans = choice(word_set)
        wordle = Wordle(ans, max_guess_times, outputs)
        for i in range(max_guess_times):
            while True:
                type_in = input(f"your answer({wordle.t}/{max_guess_times}):")
                if len(type_in) != len(ans):
                    print("only {} letter word accepted. Try again:".format(len(ans)))
                    continue
                elif type_in not in word_set:
                    print("the word is not in word set. Try again:")
                    continue
                else:
                    out = wordle.inp(type_in)
                    if out not in (0, 1):
                        print(out)
                        break
                    else:
                        break
            if out in (0, 1):
                break
        if out == 0:
            print("you lose, the answer is {}".format(ans))
        else:
            print("you win, used {} attempts".format(wordle.t-1))

if __name__ == '__main__':
    main()
