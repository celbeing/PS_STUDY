# 17243: Almost-K Increasing Subsequence
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]
