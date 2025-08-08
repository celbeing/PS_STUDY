# 17912: License to Launch
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    date = 0
    low = int(1e9)
    for i in range(n):
        if a[i] < low:
            low = a[i]
            date = i
    print(date)
solution()