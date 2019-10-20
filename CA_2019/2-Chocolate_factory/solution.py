def solve(content):
    '''
    Quadratic solution
    int with the least number of digit leading to a sum of 42 is 99996
    whenever the sum goes under this number we can stop.
    TODO: find a less compex solution
    '''
    epochs = content[1:]
    i = 0
    for e in epochs:
        if e == '42':
            i += 1
        else:
            sums = int(e)
            while sums > 99996:
                sums = sum([int(s) for s in str(sums)])
                if sums == 42:
                    i += 1
                    break
    return i
