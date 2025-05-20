#16186: Fractions
import sys
input = sys.stdin.readline
def euc(a, b):
    while b:
        a, b = b, a % b
    return a
def solution():
    count = 0
    p, q, r, s = map(int, input().split())
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            if euc(a, b) == 1:
                i = max(p // a + (1 if p % a else 0), r // b + (1 if r % b else 0))
                j = min(q // a, s // b) + 1
                if i < j:
                    count += j - i
    print(count)
solution()