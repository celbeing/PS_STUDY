import sys
from math import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def solve(t, cases):
    results = []
    for n, k in cases:
        overall_lcm = k[0]
        for ki in k[1:]:
            overall_lcm = lcm(overall_lcm, ki)

        p = [overall_lcm // ki for ki in k]
        total = sum(p)

        if all(total < ki * (overall_lcm // ki) for ki in k):
            results.append(" ".join(map(str, p)))
        else:
            results.append("-1")

    return results

input = sys.stdin.readline
index = 0
t = int(input())
index += 1
cases = []

for _ in range(t):
    n = int(input())
    index += 1
    k = list(map(int, input().split()))
    index += n
    cases.append((n, k))

results = solve(t, cases)
for result in results:
    print(result)