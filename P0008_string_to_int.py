'''
    Convert the starting contiguous [+/- digits] to integer
    only ' ' is allowed whitespace character
    return INT_MIN = (-2)**31, or INT_MAX = 2 ** 31 - 1 for overflow
'''

def myAtoi(str: str) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -1 * (2 ** 31)
    str = str.lstrip(' ')
    i = 0
    while i < len(str):
        if str[i] in ('-', '+', ' ') and i != 0: break
        if str[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+'):
            i += 1
        else:
            break
    if i == 0:
        return 0

    try:
        conv = int(str[0: i])
        if conv >= INT_MAX:
            return INT_MAX
        elif conv <= INT_MIN:
            return INT_MIN
        else:
            return conv
    except ValueError:
        return 0


if __name__ == '__main__':
    print(myAtoi('abc '))
    # print(myAtoi('4193 with words'))
    pass






