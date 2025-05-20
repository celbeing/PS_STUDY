# 1826: 연료 채우기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n = int(input())
    oil = [tuple(map(int, input().split())) for _ in range(n)]
    oil.sort()
    l, p = map(int, input().split())
    hq = []
    count = 0
    for a, b in oil:
        if p >= l: break
        if p < a:
            while p < a:
                if hq:
                    p -= heappop(hq)
                    count += 1
                else:
                    print(-1)
                    return
        if p >= a:
            heappush(hq, -b)
    while p < l:
        p -= heappop(hq)
        count += 1
    print(count)
solution()