'''
    Convert a string to a zigzag string given number of rows
    example: abcdefghij , 4 rows
    output:
    a  g
    b fh
    ce i
    d  j

'''

def convert(s: str, numRows: int) -> str:
    # index_diff = (row - 1) * 2
    # decaying_diagonal = index_diff - 2 per layer
    if numRows in (0, 1): return s
    id = (numRows - 1) * 2
    out_str = ""
    for i in range(min(len(s), numRows)):
        j = i
        dd = id - i*2
        while j < len(s):
            out_str += s[j]
            if i != 0 and i != (numRows - 1) and (j + dd) < len(s):  # note that 2 ends doesn't have inbetween characters
                out_str += s[j + dd]
            j += id

    return out_str


if __name__ == '__main__':
    print(convert('ABCD', 3))
    print(convert('ABC', 4) == 'ABC')
    print(convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
    print(convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')

    pass






