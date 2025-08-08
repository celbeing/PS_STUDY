# 6784: Multiple Choice:
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    ans = [input().strip() for _ in range(n)]
    count = 0
    for i in range(n):
        if input().strip() == ans[i]:
            count += 1
    print(count)
solution()