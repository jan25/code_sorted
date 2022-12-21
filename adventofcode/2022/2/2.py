import fileinput

guide = list(l.strip().split() for l in fileinput.input())


def val(x) -> int:
    if x in 'ABC':
        return ord(x) - ord('A') + 1
    if x in 'XYZ':
        return ord(x) - ord('X') + 1
    assert False, 'invalid move'


def lose(a: chr) -> chr:
    a = ord(a) - ord('A')
    return chr(ord('A') + (a - 1 + 3) % 3)


def win(a: chr) -> chr:
    a = ord(a) - ord('A')
    return chr(ord('A') + (a + 1) % 3)

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
# R 0 P 1 S 2


def result(a, x) -> int:
    score = 3 * (ord(x) - ord('X'))
    if x == 'X':
        return score + val(lose(a))
    if x == 'Y':
        return score + val(a)
    if x == 'Z':
        return score + val(win(a))
    assert False, 'invalid move'


print(sum(result(a, x) for a, x in guide))
