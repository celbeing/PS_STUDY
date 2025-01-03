# 1826: 연료 채우기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n = int(input())
    oil = [tuple(map(int, input().split())) for _ in range(n)]
    oil.sort(key = lambda x: (x[0], -x[1]))
    l, p = map(int, input().split())
    hq = [(-p, 0)]
    for a, b in oil:
