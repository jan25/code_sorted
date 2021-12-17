import fileinput
from functools import reduce

lines = list(l for l in fileinput.input())


def narrow(nums, i, keep, pref):
    ones = [n[i] for n in nums].count('1')
    zeros = [n[i] for n in nums].count('0')
    if ones > zeros:
        pref = keep
    elif ones < zeros:
        pref = keep ^ 1
    return [n for n in nums if int(n[i]) == pref]


oxy, i = lines[:], 0
while len(oxy) > 1:
    oxy = narrow(oxy, i, 1, 1)
    i += 1

car, i = lines[:], 0
while len(car) > 1:
    car = narrow(car, i, 0, 0)
    i += 1

print(int(f'0b{oxy[0]}', 2) * int(f'0b{car[0]}', 2))
