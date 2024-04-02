#11060: 점프점프
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
jh = deque([0])
count = [-1]*N
count[0] = 0
while jh:
    now = jh.popleft()
    jump = A[now]
    for i in range(now+1,now+jump+1):
        if i >= N: break
        if count[i] == -1 or count[i] > count[now]+1:
            jh.append(i)
            count[i] = count[now]+1
print(count[N-1])