from main import RawSolver as Solver, dw
from entropy import ged

def main(word_set=dw, outputs="CEN", entropy_file_location="default_words.entropy"):
    solver = Solver(word_set, outputs)
    entropy_dict = ged(entropy_file_location)
    entropy_dict_r = {e: w for w, e in entropy_dict.items()}
    while True:
        usr_answer = input("your answer")
        res = input("the game's result")
        print("processing...")
        solver.inp(res, usr_answer)
        print("here are all the available answers:")
        answers = [entropy_dict_r[i]+"\t"+str(i) for i in sorted([entropy_dict[i] for i in solver.get()])]
        print("words\tentropy")
        if len(answers) <= 40:
            print("\n".join(answers))
        else:
            print("\n".join(answers[:10]))
            print(".\n.\n.")
            print("\n".join(answers[-2:]))
            print("({} in total)".format(len(answers)))

if __name__ == '__main__':
    main()
