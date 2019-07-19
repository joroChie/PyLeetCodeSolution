'''
    Project Description
'''
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

def counter_example():
    # Counter iteratres to an iterable object
    # and return a dictionary showing element and number of times it appeared
    s = 'aaassssddfqwerasdfssddfe5'
    print(Counter(s))

    m_list = [1,1,1,2,3,4,4,5,5,8,8,8,8]
    print(Counter(m_list))

    # Find how many times a word appeard in a sentence
    sentence = 'this is my sentence, how many times does word appeared in my sentence, word.'


    w_list = [item for item in sentence.split()]    # TODO: Implement a regex to use only words excluding punctuations and case sensitivity
    print(Counter(w_list))
    c = Counter(w_list)
    # this is useful for getting the most_common data on a list


def defaultdic_example():
    d = defaultdict(lambda: 0)
    d['two'] = 2
    print(d['two'])
    print(d['one'])


def ordereddict_example():
    # the order of how the elements where added matters
    #
    pass


def namedtuple_example():
    #syntax namedtuple('NameOfTuple', 'SpaceDelimitedAttributes')
    Dog = namedtuple('Dog', 'age breed name')
    sam = Dog(age=2, breed='Lab', name='Sam')
    print(sam.breed)    # by attr
    print(sam[0])       # by index


if __name__ == '__main__':
    counter_example()
    defaultdic_example()
    pass






