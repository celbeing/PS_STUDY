#7869: 두 원
import sys
from math import *
input = sys.stdin.readline
xa,ya,ra,xb,yb,rb = map(float,input().split())
d = dist((xa,ya),(xb,yb))
area = 0

if d >= ra+rb:
    print("{:.3f}".format(0))
elif d + min(ra, rb) <= max(ra, rb):
    print("{:.3f}".format(pi*(min(ra, rb)**2)))
else:
    s = (ra+rb+d) / 2
    A = acos((ra**2-rb**2+d**2)/(2*ra*d))
    B = acos((rb**2-ra**2+d**2)/(2*rb*d))
    Sa = (A-sin(A*2)/2)*(ra**2)
    Sb = (B-sin(B*2)/2)*(rb**2)
    print("{:.3f}".format(Sa+Sb))