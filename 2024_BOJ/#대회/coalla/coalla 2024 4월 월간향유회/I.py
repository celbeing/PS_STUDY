# 30054: 웨이팅
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
wait = [0]*N
time = [0]*300001
cust = []
line = deque()
for _ in range(N):
    t1,t2 = map(int,input().split())
    if t1 >= t2: time[t2] = 1

    cust.append((t1,t2))

cust.sort(key = lambda x:(x[1], x[0]))
arrived = 0
passed = 0
for t in range(1,300001):
    whoin = False
    while arrived < N and cust[arrived][1] == t:
        if cust[arrived][0] == t:
            whoin = True
            wait[arrived] = t
        else:
            line.append(arrived)
        arrived += 1
    if whoin:
        continue
    if passed < len(line):
        wait[line[passed]] = t
        passed += 1
result = 0
for i in range(N):
    wait[i] -= cust[i][1]
    if wait[i] > result:
        result = wait[i]
print(result)