#26286: Football
import sys
input = sys.stdin.readline
def score(a, b, c = 1):
    for _ in range(c):
        print(f"{a}:{b}")
def solution():
    n = int(input())
    a = int(input())
    b = int(input())
    if a + b <= n:
        print(n - a - b)
        score(0, 0, n - a - b)
        score(1, 0, a)
        score(0, 1, b)
    elif n == 1:
        if a == b:
            print(1)
        else:
            print(0)
        score(a, b)
    elif n < a + b:
        print(0)
        if a <= b:
            if a < n:
                score(1, 0, a)
                n -= a
                score(0, 1, n - 1)
                score(0, b - n + 1)
            else:
                score(1, 0, n - 1)
                score(a - n + 1, b)
        else:
            if b < n:
                score(0, 1, b)
                n -= b
                score(1, 0, n - 1)
                score(a - n + 1, 0)
            else:
                score(0, 1, n - 1)
                score(a, b - n + 1)
solution()