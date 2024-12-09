# 26267: 은?행 털!자 1
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    high = 0
    count = dict()
    for _ in range(n):
        x, t, c = map(int, input().split())
        count[t - x] = count.get(t - x, 0) + c
        if count[t - x] > high:
            high = count[t - x]
    print(high)
solution()