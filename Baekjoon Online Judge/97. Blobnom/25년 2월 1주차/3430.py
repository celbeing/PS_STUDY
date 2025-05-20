# 3430: 용이 산다
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        t = [0] + list(map(int, input().split()))
        before = [0] * (n + 1)
        next = [0] * (m + 1)
        hq = []
        for i in range(1, m + 1):
            if t[i]:
                if before[t[i]]:
                    next[before[t[i]]] = i
                else:
                    heappush(hq, (i, t[i]))
                before[t[i]] = i

        lake = [1] * (n + 1)
        res = []
        for i in range(1, m + 1):
            if t[i]:
                if lake[t[i]]:
                    print('NO')
                    break
                else:
                    lake[t[i]] = 1
                    if next[i]:
                        heappush(hq, (next[i], t[i]))
            else:
                if hq:
                    k, drink = heappop(hq)
                    lake[drink] = 0
                    res.append(drink)
                else:
                    res.append(0)
        else:
            print('YES')
            print(*res)
solution()