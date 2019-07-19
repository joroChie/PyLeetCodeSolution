'''
    Problem Definition
    There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
    Solution was generalized that:
        f(n) = f(n-a) + f(n-b) + f(n-c)  ; for [a,b,c] is allowed steps and n is total steps

'''


class StepCounter:
    def __init__(self, step_count, step_allowed_list):
        self.step_count = step_count
        self.step_allowed_list = step_allowed_list
        self.step_set = set()
        self.get_number_of_steps(self.step_count, self.step_allowed_list)

    def __str__(self):
        msg = f"Set of Combinations  = {len(self.step_set)}\n"
        msg += f"{self.step_set}\n"

        return msg

    def get_number_of_steps(self, stair_length, allowed_step, current_comb = []):
        if stair_length == 0:
            self.step_set.add(tuple(current_comb))  #
            return

        for step in allowed_step:
            if step <= stair_length:
                current_comb.append(step)
                self.get_number_of_steps(stair_length - step, allowed_step, current_comb)
                current_comb.pop()  # Rebuilding List, remove last element from the recursion


def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase(n - x, X) for x in X)


def staircase2(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    print(cache)
    return cache[n]


def staircase3(stairs, allowed_steps):
    if stairs == 0:
        return 1
    elif stairs < 0:
        return 0
    else:
        ways_to_climb = [0 for _ in range(stairs + 1)]  # initialize to 0, represents each stair level
        # build this bottom up
        ways_to_climb[0] = 1
        for step_number in range(1, stairs + 1):
            ways_to_climb[step_number] += sum([ways_to_climb[step_number - s] for s in allowed_steps if s <= step_number])
        print(ways_to_climb)
        return ways_to_climb[stairs]


if __name__ == '__main__':
    pass

    steps = 20
    ways = [1, 2, 3, 5]
    # step_counter = StepCounter(steps, ways)
    # print(step_counter)

    print("Soln2 Steps Needed : " + str(staircase2(steps, ways)))
    print("Soln3 Steps Needed : " + str(staircase3(steps, ways)))

