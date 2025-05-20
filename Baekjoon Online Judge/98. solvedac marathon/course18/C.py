#19699: 소-난다!
import sys
from itertools import combinations
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    sieve = [1] * 9001
    sieve[0], sieve[1] = 0, 0
    prime = []
    for i in range(2, 9001):
        if sieve[i]:
            prime.append(i)
            for j in range(i ** 2, 9001, i):
                sieve[j] = 0

    comb = combinations(H, M)
    cow = set()
    for c in comb:
        k = sum(c)
        if sieve[k]: cow.add(k)
    res = sorted(list(cow))
    if res: print(*res)
    else: print(-1)
solution()