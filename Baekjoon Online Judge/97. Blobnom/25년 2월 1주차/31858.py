# 31858: 간단한 순열 문제
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    p = list(map(int, input().split()))
    stack = []
    count = 0
    for a in p:
        while stack and stack[-1] > a:
            count += 1
            stack.pop()
        stack.append(a)
        count += 1
    print(count)
    return
solution()