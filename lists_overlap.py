from typing import Union


import random
a = range(random.randint(15,40), random.randint(35,50))
b = range(random.randint(1,30), random.randint(25,50))
print(list(a))
print(list(b))
print(list(set(a) & set(b)))
