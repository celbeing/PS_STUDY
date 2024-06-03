# 1258: 문제 할당
import sys
input = sys.stdin.readline
N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
flow = [[0]*N for _ in range(N)]
