import sys
from itertools import combinations
input = sys.stdin.readline

def ccw(a,b,c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return 1
    else: return -1

N = int(input())
cave = [tuple(map(int,input().split())) for _ in range(N)]
cave.sort()
count = 0
comb = list(combinations(cave,4))
for r in comb:
    a = ccw(r[0],r[1],r[2])+ccw(r[1],r[2],r[3])+ccw(r[2],r[3],r[0])+ccw(r[3],r[0],r[1])
    b = ccw(r[0],r[1],r[3])+ccw(r[1],r[3],r[2])+ccw(r[3],r[2],r[0])+ccw(r[2],r[0],r[1])
    if abs(a) == 4: count += 1
    elif abs(b) == 4: count += 1
print(count)