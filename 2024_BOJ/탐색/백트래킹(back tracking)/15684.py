#15684: 사다리 조작
import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
ladder= [[0]*(H+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    ladder[b][a] = 1
result = H*(N-1)-M+1

def Ladder(l):
    for i in range(1,N+1):
        t = i
        for j in range(1,H+1):
            if l[t][j] == 1:
                t += 1
            elif l[t-1][j] == 1:
                t -= 1
        if t != i:
            return False
    else:
        return True

def DFS(l,k,c,h):
    if k > 3:
        return result
    if Ladder(l):
        return k
    r = result
    for j in range(h+1,H+1):
        if l[c][j] == l[c-1][j] == l[c+1][j] == 0:
            l[c][j] = 1
            r = min(DFS(l,k+1,c,j),r)
            l[c][j] = 0

    for i in range(c+1,N):
        for j in range(1,H+1):
            if l[i][j] == l[i-1][j] == l[i+1][j] == 0:
                l[i][j] = 1
                r = min(DFS(l,k+1,i,j),r)
                l[i][j] = 0
    return r

result = DFS(ladder,0,1,0)
if result > (N-1)*H-M or result > 3 : result = -1
print(result)