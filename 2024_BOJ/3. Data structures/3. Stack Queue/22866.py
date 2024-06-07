#22866: 탑 보기
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
tower = list(map(int,input().split()))
count = [0 for _ in range(N)]
sight = [i for i in range(N)]

stack = deque([0])
for i in range(1,N):
    if tower[i] >= tower[stack[-1]]:
        while stack and tower[i] >= tower[stack[-1]]:
            stack.pop()
    count[i] += len(stack)
    if stack: sight[i] = stack[-1]
    stack.append(i)

stack = deque([N-1])
for i in range(N-2,-1,-1):
    if tower[i] >= tower[stack[-1]]:
        while stack and tower[i] >= tower[stack[-1]]:
            stack.pop()
    count[i] += len(stack)
    if stack and i != sight[i]:
        if i - sight[i] > stack[-1] - i:
            sight[i] = stack[-1]
    elif stack:
        sight[i] = stack[-1]
    stack.append(i)

for i in range(N):
    if count[i] == 0:
        print(0)
    else:
        print(count[i],sight[i]+1)