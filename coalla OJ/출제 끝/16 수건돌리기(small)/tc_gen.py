import random
from collections import deque
random.random()
path = "C:\\Users\\kimsd\\OneDrive\\문서\\GitHub\\2024_BOJ\\coalla OJ\\16 수건돌리기(small)\\"
k = 3
for _ in range(50):
    n = random.randint(1, 1000)
    m = random.randint(0, 1000)
    file = open(path + f"{k}.in", 'w')
    w = file.writelines(f"{n} {m}")
    dq = deque([i for i in range(1, n + 1)])
    for i in range(n - 1):
        for j in range(m):
            dq.append(dq.popleft())
        dq.popleft()
    file = open(path + f"{k}.out", 'w')
    w = file.writelines(f"{dq[0]}")
    k += 1