# 15485: a^jb^jc^k
import sys
input = sys.stdin.readline
def solution():
    s = list(input().strip())
    dp = [[0] * 4 for _ in range(len(s) + 1)]
    dp[0][0] = 1
    
