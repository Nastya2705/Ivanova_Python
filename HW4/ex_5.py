
from functools import reduce

def my_set (prev_el, el):

    return prev_el + el
print(reduce(my_set, {el for el in range(99, 1001) if el % 2 == 0}))