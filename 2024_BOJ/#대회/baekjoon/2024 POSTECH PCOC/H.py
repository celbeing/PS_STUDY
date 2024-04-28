# H: 저체온증
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
p = [list(input().rstirp()) for _ in range(N)]

for i in range(N*M):
    r = i//M
    c = i%M
