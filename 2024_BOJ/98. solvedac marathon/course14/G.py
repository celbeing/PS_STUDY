#16158: 회식구호
import sys
from fractions import Fraction
input = sys.stdin.readline
def satisfy(P, X):
    D1 = Fraction(X * P, 100)
    D2 = Fraction(P * 2, 1) - D1
    return min(D1, D2), max(D1, D2)

def solution():
    N, X, K = map(int, input().split())
    loud = list(map(int, input().split()))
    l, r = satisfy(loud[0], X)
    for i in range(1, N):
        nl, nr = satisfy(loud[i], X)
        if nl > r or nr < l:
            print(-1)
            return
        if l < nl: l = nl
        if nr < r: r = nr
    print(nl)

solution()