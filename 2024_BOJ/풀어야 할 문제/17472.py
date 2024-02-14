#17472: 다리 만들기 2
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
island = [[] for _ in range(6)]
d = [(0,1),(1,0),(0,-1),(-1,0)]
