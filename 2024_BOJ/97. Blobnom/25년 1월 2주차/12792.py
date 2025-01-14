# 12792: 주작 주 주작
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    j = list(map(int, input().split()))
    for i in range(n):
        if j[i] == i + 1:
            print(-1)
            return
    print(1000003)
solution()