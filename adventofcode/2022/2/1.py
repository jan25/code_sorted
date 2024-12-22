import fileinput

guide = list(l.strip().split() for l in fileinput.input())


def val(x) -> int:
    if x in 'ABC':
        return ord(x) - ord('A') + 1
    if x in 'XYZ':
        return ord(x) - ord('X') + 1
    assert False, 'invalid move'


# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# R 0 P 1 S 2
def result(a, x) -> int:
    a, x = val(a) - 1, val(x) - 1
    if a == x:
        return 3
    if (x, a) in {(0, 2), (2, 1), (1, 0)}:
        return 6
    return 0


print(sum(val(x) + result(a, x) for a, x in guide))
