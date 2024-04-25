#14881: 물통 문제
import sys
from math import gcd
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    g = gcd(a,b)
    flag = False
    if c > a and c > b: flag = False
    elif c == a or c == b: flag = True
    elif c%g == 0: flag = True
    elif g == 1: flag = True
    if flag:
        print("YES")
    else:
        print("NO")