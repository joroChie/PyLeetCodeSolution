'''
    Project Description
'''


def intToRoman(num: int) -> str:
    # limit the input to 3999

    if not (1 <= num <= 3999):
        return ""

    numstr = str(num)[::-1]
    roman = ""

    lookup = (
        ('', 'I','II','III','IV','V','VI','VII','VIII','IX'),
        ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
        ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
        ('', 'M', 'MM', 'MMM')
    )

    for idx, digit in enumerate(numstr):
        roman = lookup[idx][int(digit)] + roman

    return roman





if __name__ == '__main__':
    print(intToRoman(3999))
    pass






