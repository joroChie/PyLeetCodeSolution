'''
    Reverses an integer
    123 -> 321
    -123 -> -321
'''

def reverse(x: int) -> int:
    if x == 0: return x
    multiplier = 1
    if x < 0:
        multiplier = -1
        x *= multiplier
    s = f'{x}'[::-1]
    rev = int(s) * multiplier
    print(rev)
    print(2**31)
    if rev > 2 ** 31: return 0
    return rev


if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(-2147483648))
    pass






