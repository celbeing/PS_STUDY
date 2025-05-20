# 14856: 조금 똑똑한 뢰벗과 조금 잘생긴 사냐
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    fib = deque([1, 2])
    N = int(input())
    while fib[-1] + fib[-2] <= N:
        fib.append(fib[-1] + fib[-2])
    result = []
    while fib:
        if fib[-1] <= N:
            result.append(fib.pop())
            N -= result[-1]
        else:
            fib.pop()
    print(len(result))
    result.reverse()
    print(*result)
solution()