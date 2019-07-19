'''
    Scratch note for Decorator Concept
'''


def func_dec(this_func):

    def wrapper():
        print('Start Decor')
        this_func()
        print('End Decor')

    return wrapper


@func_dec
def my_func():
    print('Original Func')


if __name__ == '__main__':
    my_func()
    pass






