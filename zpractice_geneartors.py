'''
    Project Description
'''

import random

def sample():
    # This doesn't create a list of one to 10
    # Instead, it keeps track of the last number and
    # increment to the next number in range using the stepsize
    for i in range(0, 10):
        print(i)

    # this however generates a list in the memory
    new_list = list(range(0, 10))
    for i in new_list:
        print(i)


# Normally, you would need a list object
# append the result on the list
def create_cube_normal(n):
    result = []
    for i in range(n):
        result.append(i ** 3)

    return result


# Using Yield, it just generates
# the cube value as it comes
def create_cube_generator(n):
    for i in range(n):
        yield i ** 3


def generate_fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a # this will jump out of this function to return intermidiate result, then continue the remaining loop and code
        a, b = b, a + b


def rand_gen(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


if __name__ == '__main__':

    # number is a variable to store
    # intermidiate result of generate_fibo()
    # for number in generate_fibo(5):
    #     print(number)
    # pass


    # generate random
    for i in rand_gen(5, 10, 5):
        print(i)

    # generator comprehension, switch the [] with ()
    gencomp = (item for item in range(10) if item > 5)

    for n in gencomp:
        print(n)



