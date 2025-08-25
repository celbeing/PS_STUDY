import random
from collections import deque
path = "C:\\Users\\kimsd\\OneDrive\\문서\\GitHub\\2024_BOJ\\coalla OJ\\18 콜라츠의 꼭대기\\"

for i in range(1, 101):
    file = open(path + f'{i}.in', 'w+')
    r = random.randint(1, 100000000)
    w = file.writelines(f'{r}')
    res = r
    while r > 1:
        if r & 1:
            r *= 3
            r += 1
        else:
            r //= 2
        res = max(r, res)
    file = open(path + f'{i}.out', 'w+')
    w = file.writelines(f'{res}')