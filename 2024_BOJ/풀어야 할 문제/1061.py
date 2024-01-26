#1061: 삼각형
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
dot = [list(map(str,input().rstrip())) for _ in range(N)]
result = 0

def area(a,b,c):
    return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-b[0]*a[1]-c[0]*b[1]-a[0]*c[1])

def find(a,b,c):
    A = area(a,b,c)
    B = 0
    for i in range(M*N):
        k = [i//M,i%M]
        if k == a or k == b or k == c: continue
        if dot[a[0]][a[1]] == dot[k[0]][k[1]]:
            B = area(k,b,c)
        elif dot[b[0]][b[1]] == dot[k[0]][k[1]]:
            B = area(a,k,c)
        else:
            B = area(a,b,k)
        if B > A:
            return True
    return False

for i in range(M*N-1):
    a = [i//M,i%M]
    for j in range(i+1,N*M):
        b = [j//M,j%M]
        if dot[a[0]][a[1]] == dot[b[0]][b[1]]:
            continue
        for k in range(j+1,M*N):
            c = [k//M,k%M]
            if dot[c[0]][c[1]] == dot[a[0]][a[1]] or dot[c[0]][c[1]] == dot[b[0]][b[1]]:
                continue

            if find(a,b,c):
                result += 1

print(result)