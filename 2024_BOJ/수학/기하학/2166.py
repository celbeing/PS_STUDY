#2166: 다각형의 면적
import sys
input = sys.stdin.readline
N = int(input())
area = 0
x,y = map(int,input().split())
a,b = x,y
for _ in range(N-1):
    p,q = map(int,input().split())
    area += (p-a)*(q+b)
    a,b = p,q
area += (x-a)*(y+b)
print("{:.1f}".format(abs(round(area/2,1))))