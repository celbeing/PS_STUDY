import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
carrot = [tuple(map(int,input().split())) for _ in range(N)]
carrot.sort()
memo = [[0,0] for i in range(K+1)]
bfs = deque([(0,1,0)])
record = 0
while bfs:
    time, speed, have = bfs.popleft()
    if time == K-1:
        if have+speed > record:
            record = have+speed
        continue
    if memo[time+1][0] >= speed and memo[time+1][1] >= have: continue
    if memo[time+1][0] < speed and memo[time+1][1] < have:
        memo[time+1][0] = speed
        memo[time+1][1] = have
    bfs.append((time+1,speed,have+speed))
    for pay,get in carrot:
        if pay > have: break
        next = (time+1,speed+get,have-pay)
        if next in bfs: continue
        bfs.append(next)
print(record)