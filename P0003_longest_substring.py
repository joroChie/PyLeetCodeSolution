# Length of longest substring without repeating character


def len_longest_substring(s):
    if s == "": return 0
    if len(s) == 1: return 1

    start, longest = 0, 0
    seen = {}

    for end, char in enumerate(s):
        if char not in seen:
            seen[char] = end
        else:
            start = max(start, seen[char] + 1)
            seen[char] = end
        longest = max(longest, (end - start) + 1)

    return longest


def length_longest_substring(s):
    if s == "":
        return 0
    if len(s) == 1:
        return 1
    dletter = {}
    start_idx = 0
    longest = 1
    lstr = ""

    for idx, char in enumerate(s):
        if char in lstr:
            start_idx = dletter[char] + 1
        lstr = s[start_idx: idx + 1]
        longest = max(longest, idx + 1 - start_idx)
        dletter[char] = idx

    return longest


if __name__ == '__main__':
    s = 'abba'
    print(len_longest_substring(s))