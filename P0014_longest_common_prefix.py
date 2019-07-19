'''
    Project Description
'''


def longestCommonPrefix(strs):
    longest_prefix = ""
    pos = 0
    flag_same = True
    while flag_same:
        letter_set = set()
        for word in strs:
            if pos < len(word):
                letter_set.add(word[pos])
            else:
                flag_same = False
                break
        if len(letter_set) == 1 and flag_same:
            longest_prefix += letter_set.pop()
            pos += 1
        else:
            flag_same = False

    return longest_prefix


# using list comprehension
def longestCommonPrefix2(strs):
    if len(strs) == 1:
        return strs[0]
    if len(strs) == 0:
        return ""
    letters = []
    print(min(strs, key=len))
    min_len = len(min(strs, key=len))

    for i in range(min_len):
        temp_list = set([word[i] for word in strs])
        if len(temp_list) > 1:
            break
        else:
            letters.append(temp_list.pop())

    return "".join(letters)


if __name__ == '__main__':
    strs = ["flower", "fla", "flower"]
    #strs = []
    print(longestCommonPrefix2(strs))



    pass






