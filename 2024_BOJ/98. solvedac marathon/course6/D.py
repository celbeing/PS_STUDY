import sys
input = sys.stdin.readline
S = list(input().rstrip())
L = len(S)-1
N,M = map(int,input().split())
B = [list(input().rstrip()) for _ in range(N)]
d = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
for i in range(N):
    for j in range(M):
        for k in range(8):
            dx,dy = d[k]
            if B[i][j] == S[0] and 0<=L*dx+i<N and 0<=L*dy+j<M:
                dx,dy = i+d[k][0],j+d[k][1]
                for t in range(1,L+1):
                    if B[dx][dy] == S[t]:
                        dx += d[k][0]
                        dy += d[k][1]
                    else:
                        break
                else:
                    print(1)
                    exit()
print(0)