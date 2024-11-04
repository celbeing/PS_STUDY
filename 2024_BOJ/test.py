import sys, random
from collections import deque
input = sys.stdin.readline
def solution():
<<<<<<< Updated upstream
    n = input().strip()
    res = "1"
    k = 2
    while int(res) < int(n):
        res += str(k)
        k += 1
    if res == n:
        print(k - 1)
    else: print(-1)
=======
    n = int(input())
    ori = deque([i for i in range(1, n + 1)])
    random.random()
    random.shuffle(ori)
    print(ori)
>>>>>>> Stashed changes
solution()