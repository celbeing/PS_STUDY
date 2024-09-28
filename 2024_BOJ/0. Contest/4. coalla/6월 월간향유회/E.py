import sys
input = sys.stdin.readline
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]

def pooling(r,c,d):
    if d == 1:
        k = [mat[r][c],mat[r+d][c],mat[r][c+d],mat[r+d][c+d]]
        k.sort()
        return k[-2]
    t = d//2
    k = [pooling(r,c,t),pooling(r+d,c,t),pooling(r,c+d,t),pooling(r+d,c+d,t)]
    k.sort()
    return k[-2]

print(pooling(0,0,N//2))