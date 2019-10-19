
def solve2(content):
    '''
    0(n) : "Brut force" solving way
    For each integer between A and B check if it is divisible by D.
    '''
    A, B, D = int(content[0]), int(content[1]), int(content[2])
    for i in range(A, B+1):
        if i % D == 0:
            return i
    return None


def solve(content):
    '''
    O(1): Checks at most two values
    first divisible number after A by D is A + (D - A%D)
    e.g.
    A = 8, B= 18, D = 7
    A%D == 1
    A + D -1 = 8 + 6 = 14
    A<14<B => OK
    '''
    A, B, D = int(content[0]), int(content[1]), int(content[2])
    while A <= B:
        if A % D == 0:
            return A
        else:
            A += D-A % D
    return None
