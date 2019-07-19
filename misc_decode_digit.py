'''
    Problem : Return how many ways a string can be decoded given that:
    a -> 1
    b -> 2
    .
    z -> 26

    example:
    data = "12" returns 2 since there are 2 ways these can be decoded, 'ab' or 'l'

    Solution should be comply with O(n) time complexity
'''

# Using memoization


def num_ways_dp(data):
    memo = [0 for _ in range(len(data) + 1)]
    ways = helper_dp(data, memo)
    print(memo)
    return ways


def helper_dp(data, memo):

    if data == "":
        return 1

    if data[0] == '0':
        return 0

    if memo[len(data)] != 0:  # this avoids deep recursion
        return memo[len(data)]

    result = helper_dp(data[1:], memo)
    if len(data) >= 2 and int(data[:1]) <= 26:
        result += helper_dp(data[2:], memo)

    memo[len(data)] = result  # save data for later use
    return result


if __name__ == '__main__':
    ipt = '1211'

    res2 = num_ways_dp(ipt)
    print(f"SOLN2: data = {ipt} decoded {res2} times")