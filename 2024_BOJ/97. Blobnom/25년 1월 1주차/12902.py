# 12902: Alice and Bob
import sys
input = sys.stdin.readline
def solution():
    n = int(input().split())
    c = list(map(int, input().split()))
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            a = c[i]
            b = c[j]
            while 