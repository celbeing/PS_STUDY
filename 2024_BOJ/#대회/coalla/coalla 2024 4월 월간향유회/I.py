# 30054: 웨이팅
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
time = 0
wait = [0]*(N+1)
rsrv = deque()
for _ in range(N):
    t1,t2 = map(int,input().split())
    rsrv.append((t2,t1))
rsrv.sort()