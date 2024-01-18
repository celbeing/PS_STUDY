#1061: 삼각형
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dot = [list(map(str,input().rstrip())) for _ in range(N)]
rgb = ['R','G','B']
result = 0

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    return abs(k)

for i in range(M*N-1):
    a = [i//M,i%M]
    for j in range(i+1,N*M):
        b = [j//M,j%M]
        if dot[a[0]][a[1]] == dot[b[0]][b[1]]: continue
        t = rgb[3-rgb.index(dot[a[0]][a[1]])-rgb.index(dot[b[0]][b[1]])]
        peek = 0
        count = 0
        top = 0
        for k in range(M*N):
            c = [k//M,k%M]
            if a == c or b == c or dot[c[0]][c[1]] != t: continue
            deg = ccw(a,c,b)
            if deg > peek:
                peek = deg
                top = 1
            elif deg == peek:
                top += 1
            count += 1
        result += count - top

print(result)