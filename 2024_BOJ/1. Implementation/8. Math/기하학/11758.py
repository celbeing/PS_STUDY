#11758: CCW
import sys
input = sys.stdin.readline
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
c = tuple(map(int,input().split()))
ccw = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
if ccw < 0: print(1)
elif ccw > 0: print(-1)
else: print(0)