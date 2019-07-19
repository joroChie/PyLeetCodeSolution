import time


def time_it(func):
    def wrapper(*args, **kwargs):
        ts = time.time()
        res = func(*args, **kwargs)
        te = time.time()
        print(f'method:\n\t{func}')
        print(f'Input:\n\t{args} {kwargs}')
        print(f'Output:')
        print(f'\t {res}')
        tl = (te - ts)*1000
        print(f'\nExecution time : {tl:.3f} ms')
    return wrapper


@time_it
def twosum(nums, target):
    comps = []  # holds complimentary of current index
    for idx, num in enumerate(nums):
        if num in comps:
            return [comps.index(num), idx]
        comps.append(target - num)
    return []


if __name__ == '__main__':
    mlist = [2, 7, 11, 15]
    twosum(mlist, 9)








