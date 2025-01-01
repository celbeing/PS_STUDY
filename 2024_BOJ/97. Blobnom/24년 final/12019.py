# 12019: 동아리방 청소!
import sys
input = sys.stdin.readline
def solution():
    inf = 
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(n):
