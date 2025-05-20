# 30054: 웨이팅
import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
customer = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x: (x[1], x[0]))
index = 0
time = 0
early = []
late = deque([])
arrived = [-1]*(200001)
entered = [-1]*(200001)
while time < 300001:
    while index < N and customer[index][1] == time:
        if customer[index][0] < time:
            late.append(customer[index])
        else:
            late.append(customer[index])
            heappush(early,customer[index])
        arrived[customer[index][0]] = time
        index += 1
    poss = True
    if early:
        while early and entered[early[0][0]] > 0:
            heappop(early)
        if early and early[0][0] == time:
            entered[heappop(early)[0]] = time
            poss = False
    if poss and late:
        while late and entered[late[0][0]] > 0:
            late.popleft()
        if late:
            entered[late.popleft()[0]] = time
    time += 1

longest = 0
for i in range(1,200001):
    wait = entered[i]-arrived[i]
    if longest < wait: longest = wait

print(longest)