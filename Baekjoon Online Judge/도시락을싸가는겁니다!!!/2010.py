# 2010: 플러그
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    s = sum([int(input()) for _ in range(n)]) - n + 1
    print(s)
solution()