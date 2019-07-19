'''
    Project Description
'''


def longest_palindrome(s: str) -> str:
    s = s.lower()
    longest = s[0]

    for idx, char in enumerate(s):
        for idx2 in range(idx + 1, len(s)):
            if char == s[idx2] and is_palindrome(s[idx:idx2 + 1]):
                if len(longest) < len(s[idx:idx2 + 1]):
                    longest = s[idx:idx2 + 1]

    return longest


def is_palindrome(s: str):
    return s == s[::-1]


if __name__ == '__main__':
    pass

    print(longest_palindrome("bab"))




