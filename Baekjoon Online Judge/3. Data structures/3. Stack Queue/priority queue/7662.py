#7662: 이중 우선순위 큐
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    minh = []
    maxh = []
    check = dict()
    count = 0
    for _ in range(k):
        Q = list(input().split())
        if Q[0] == 'I':
            n = int(Q[1])
            heappush(minh,n)
            heappush(maxh,-n)
            n += 1<<31
            if n in check:
                check[n] += 1
            else:
                check[n] = 1
            count += 1

        else:
            if count == 0:
                continue

            if Q[1] == '1':
                t = -heappop(maxh)
                check[t+(1<<31)] -= 1
                count -= 1

            else:
                t = heappop(minh)
                check[t+(1<<31)] -= 1
                count -= 1

            while maxh and check[-maxh[0]+(1<<31)] == 0: heappop(maxh)
            while minh and check[minh[0]+(1<<31)] == 0: heappop(minh)

    if count == 0:
        print("EMPTY")
    else:
        print(-maxh[0],minh[0])