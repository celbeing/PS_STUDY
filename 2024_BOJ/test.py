import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        c, p = map(int, input().split())
        print(c, p)
        print(p if c == 1 else c * p - (c - 1) * 2)
solution()