# 8138: Tourist Attractions
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 다익스트라로 사이트(1~k+1,n) 별 거리 확인
# 제약 확인
# tsp
# 너무 쉬운데..? 왜 P1..?