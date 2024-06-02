import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N,M,K = map(int,input().split())
work = []
for _ in range(N):
    heappush(work,-int(input()))
sat = [0]
count = 0
while work:
    today = -heappop(work)
    sat.append(sat[-1]//2 + today)
    today -= M
    if today > K: heappush(work,-today)
day = len(sat)-1
print(day)
for i in range(1,day+1):
    print(sat[i])