from os import listdir
from os.path import isfile, join
import solution as sol
import timeit


def test():
    input_files = [join("samples", f) for f in listdir("samples") if "input" in f and isfile(join("samples", f))]
    for f in input_files:
        solution = open(f.replace('input', 'output')).readline()
        with open(f) as file:
            content = [line.rstrip('\n') for line in file]
        ret = sol.solve(content)
        print('Expected: ' + str(solution))
        print('Found: ' + str(ret))
        if not str(solution).strip() == str(ret).strip():
            print('Wrong !')
            return
    print('Success !')


if __name__ == "__main__":
    # print(str(timeit.timeit(test, number=100)/100))
    test()
