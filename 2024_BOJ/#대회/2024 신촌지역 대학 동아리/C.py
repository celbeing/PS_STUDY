# C: 스펀지
import sys
input = sys.stdin.readline
W,H,K,T = map(int,input().split())
case = 1
for _ in range(K):
    x,y = map(int,input().split())
    lx = x-T
    if lx < 1: lx = 1
    ly = y-T
    if ly < 1: ly = 1
    rx = x+T
    if rx > W: rx = W
    ry = y+T
    if ry > H: ry = H
    case *= (rx-lx+1)*(ry-ly+1)%998_244_353
    case %= 998_244_353
print(case)