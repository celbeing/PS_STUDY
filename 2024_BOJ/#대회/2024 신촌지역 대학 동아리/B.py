# B: 가장 짧은 높이
import sys
input = sys.stdin.readline
N = int(input())
dot = [tuple(map(int,input().split())) for _ in range(N)]

def height(a,b,c):
    area = abs((a[0]*b[1]+b[0]*c[1]+c[0]*a[1]) - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0]))
    l = ((a[0]-b[0])**2 + (a[1]-b[1])**2)
    bc = ((b[0]-c[0])**2 + (b[1]-c[1])**2)
    if l < bc: l = bc
    ca = ((c[0]-a[0])**2 + (c[1]-a[1])**2)
    if l < ca: l = ca
    return area / l**0.5

result = 1e10
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            h = height(dot[i],dot[j],dot[k])
            if result > h:
                result = h

print(result)