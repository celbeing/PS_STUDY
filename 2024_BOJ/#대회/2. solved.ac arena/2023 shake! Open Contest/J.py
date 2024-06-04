#J: 볼록볼록
import sys
from collections import deque

def direction(a,b,c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k < 0:
        return True
    else:
        return False

input = sys.stdin.readline
N = int(input())
peek = -1
dot = deque()
for _ in range(N):
    dot.append(tuple(map(int, input().split())))
    if len(dot) < 3:
        continue
    else:
        if direction(dot[-3],dot[-2],dot[-1]):
            while len(dot) >= 3 and (not(direction(dot[-2],dot[-1],dot[0])) or not(direction(dot[-1],dot[0],dot[1]))):
                dot.popleft()
            if len(dot) >= 3 and len(dot) > peek:
                peek = len(dot)
        else:
            k = len(dot)
            for _ in range(k-2):
                dot.popleft()

print(peek)