from math import factorial
from itertools import count
def fibo_gen():
    for el in count(1):
        yield factorial(el)
gen = fibo_gen()
x = 0
for i in gen:
    if x < 5:
        print(i)
        x += 1
    else:
        break

