'''
    Project Description
'''

def romanToInt(s: str) -> int:

    if s == "":
        return 0

    symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if len(s) == 1:
        return symbol[s]

    curr_val, total = 0, 0
    for char in s[::-1]:
        val = symbol[char]
        if val >= curr_val:
            total += val
        else:
            total -= val

        curr_val = val

    return total


if __name__ == '__main__':
    print(romanToInt('D'))
    pass






