import fileinput

code = next(fileinput.input()).strip()
print(len(code))


def tobin(x: str):
    if x.isalpha():
        x = 10 + ord(x) - ord('A')
    x = int(x)
    b = bin(x)[2:]
    return '0' * (4 - len(b)) + b


assert tobin('9') == '1001'
assert tobin('A') == '1010'
assert tobin('F') == '1111'


def toi(b: str):
    return int('0b' + b, base=2)


def sub(l, r, size=None):
    if not size:
        size = r - l + 1

    while size // 11 > 1:
        yield l, l + 10
        l += 11
        size -= 11
    yield l, r


def parse(c, l, r):
    print(c[l: r + 1])
    ver = toi(c[l: l + 3])
    t = toi(c[l + 3: l + 6])
    print(f'ver={ver} type={t}')
    if t == 4:
        print('literal type')
        # literal values
        return ver

    if c[l + 6] == '0':
        print('0 type')
        size = toi(c[l + 7: l + 7 + 15])
        for nl, nr in sub(l + 7 + 15, r, size):
            print('subpacket', c[nl: nr + 1])
            ver += parse(c, nl, nr)

    if c[l + 6] == '1':
        print('1 type')
        count = toi(c[l + 7: l + 7 + 11])
        for nl, nr in sub(l + 7 + 11, r):
            if count == 0:
                break
            print('subpacket', c[nl: nr + 1])
            count -= 1
            ver += parse(c, nl, nr)

    return ver


def decode(code):
    return ''.join(map(tobin, code))


assert decode(
    'EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000'
assert decode(
    '38006F45291200') == '00111000000000000110111101000101001010010001001000000000'

bits = decode(code)
print(bits)
print(parse(bits, 0, len(bits) - 1))
