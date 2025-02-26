from itertools import count
from math import gcd

number, x = 4020433, 2

for cycle in count(1):
    y = x
    for i in range(2 ** cycle):
        x = (x * x + 1) % number
        factor = gcd(x - y, number)
        if factor > 1:
            print("factor is", factor)
            exit()