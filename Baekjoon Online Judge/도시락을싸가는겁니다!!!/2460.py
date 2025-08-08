# 2460: 지능형 기차 2
import sys
input = sys.stdin.readline
def solution():
    high = 0
    passenger = 0
    for _ in range(10):
        a, b = map(int, input().split())
        passenger += b - a
        if high < passenger: high = passenger
    print(high)
solution()