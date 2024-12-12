import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    M = list(input().rstrip())
    K = int(input())
    if K and '1' in M[-min(N, K):]: print('NO')
    else: print('YES')
solution()