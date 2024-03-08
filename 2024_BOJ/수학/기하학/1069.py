#1069: 집으로
import sys
from math import *
input = sys.stdin.readline
X,Y,D,T = map(int,input().split())
d = dist((0,0),(X,Y))
jw = d//D*T+d%D
wj = jw+T+D-d%D*2
jj = T*2
if d / D > 2:
    jj += (d // D - 1)*T
print(min(d,jw,wj,jj))