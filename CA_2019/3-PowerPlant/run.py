from os import listdir
from os.path import isfile, join, dirname, realpath, basename
import solution as sol
import timeit

dir_path = join(dirname(realpath(__file__)), "samples")

def test():
    input_files = [join(dir_path, f) for f in listdir(dir_path) if "input5" in f and isfile(join(dir_path, f))]
    for f in input_files:
        print('======   '+str(basename(f))+'   =====')
        solution = open(f.replace('input', 'output')).readline()
        with open(f) as file:
            content = [line.rstrip('\n') for line in file]
        ret = sol.solve(content)
        print('Expected: ' + str(solution))
        print('Found: ' + str(ret))
        if not str(solution).strip() == str(ret).strip():
            print('Wrong !')
    print('Success !')


if __name__ == "__main__":
    # print(str(timeit.timeit(test, number=100)/100))
    test()
