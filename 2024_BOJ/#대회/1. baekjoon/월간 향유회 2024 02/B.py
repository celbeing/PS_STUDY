#B: 줄다리기
import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input().split())
n = [i for i in range(N)]
teamwork = [list(map(int,input().split())) for _ in range(N)]
record = 0
t = N//2
comb = list(combinations(n,t))

for team in teamwork:
    low = 1_000_000
    othor = []
    for i in range(t):
