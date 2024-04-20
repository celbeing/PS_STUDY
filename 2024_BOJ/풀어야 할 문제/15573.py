#15573: 채굴
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N,M,K = map(int,input().split())
S = [list(map(int,input().split())) for _ in range(N)]
mine = [[0]*M for _ in range(N)]
heap = []