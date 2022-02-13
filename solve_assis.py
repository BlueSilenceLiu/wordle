from main import RawSolver as Solver, dw

def main(word_set=dw, outputs="CEN"):
    solver = Solver(word_set, outputs)
    while True:
        usr_answer = input("your answer")
        res = input("the game's result")
        print("processing...")
        solver.inp(res, usr_answer)
        print("here are all the available answers:")
        answers = solver.get()
        if len(answers) <= 40:
            print("\n".join(answers))
        else:
            print("\n".join(answers[:10]))
            print(".\n.\n.")
            print("\n".join(answers[-2:]))
            print("({} in total)".format(len(answers)))

if __name__ == '__main__':
    main()
