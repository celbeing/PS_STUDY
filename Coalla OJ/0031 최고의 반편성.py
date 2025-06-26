import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
f = [sorted(list(map(int, input().split()))) for _ in range(n)]
idx = [0] * n
high = 0
hq = []
for i in range(n):
    heappush(hq, (f[i][0], i))
    high = max(high, f[i][0])
res = 10**9
while True:
    low, i = heappop(hq)
    res = min(res, high - low)
    idx[i] += 1
    if idx[i] == m[i]: break
    high = max(high, f[i][idx[i]])
    heappush(hq, (f[i][idx[i]], i))
print(res)