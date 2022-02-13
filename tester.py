from main import Wordle, dw
from solver import Solver
from time import perf_counter

win = 0
attempts = [0]*10
total_time = 0
for i in range(len(dw)):
    wordle = Wordle(dw[i], mxt=100)
    solver = Solver()
    cb = perf_counter()
    while True:
        type_in = solver.get()
        out = wordle.inp(type_in)
        if type(out) == str:
            solver.inp(out, type_in)
        else:
            attempts[wordle.t - 2] += 1
            if wordle.t - 1 <= 6:
                win += 1
            break
    ce = perf_counter()
    total_time += ce - cb
    print(f"{i+1}/{len(dw)}  remaining: {(len(dw)-i-1)/(i+1)*total_time}s")
print(attempts)
print(f"win rate: {win / len(dw) * 100}%")
print(f"average score: {sum([(i+1)*attempts[i] for i in range(len(attempts))])/len(dw)}")
print(f"average time: {total_time / len(dw)}s")
