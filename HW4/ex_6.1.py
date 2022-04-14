from itertools import cycle
c = 0
for el in cycle("123"):
    if c > 15:
        break
    print(el)
    c+= 1