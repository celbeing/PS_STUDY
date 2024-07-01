import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = sorted(list(map(int,input().split())))
stack = []
result = []
money = deque(B)
money.append(int(1e9))
for i in range(N):
    while A[i] > money[0]:
        stack.append(money.popleft())
    if money[0] == int(1e9):
        result.clear()
        break
    else:
        result.append(money.popleft())
    while stack:
        money.appendleft(stack.pop())
if result:
    print(*result)
else:
    print(-1)