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
        if a < n:
            score(1, 0, a)
            score(0, 1, n - a - 1)
            score(0, b - n + a + 1)
        elif b < n:
            score(0, 1, b)
            score(1, 0, n - b - 1)
            score(a - n + b + 1, 0)
        else:
            