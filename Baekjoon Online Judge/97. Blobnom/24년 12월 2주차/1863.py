# 1863: 스카이라인 쉬운거
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    stack = deque([0])
    count = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if y < stack[-1]:
            while stack[-1] > y:
                stack.pop()
                count += 1
        if y > stack[-1]:
            stack.append(y)
    count += len(stack) - 1
    print(count)
solution()