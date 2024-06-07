import sys
input = sys.stdin.readline
N,M = map(int,input().split())
QA = [tuple(map(str,input().split())) for _ in range(N)]
QA.sort()
for _ in range(M):
    S = input().rstip()