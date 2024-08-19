#13247: 토끼의 이동
import sys
input = sys.stdin.readline
board = list(input().rstrip())
r = int(input())
N = len(board)

def simulate(rabbits):
    rabbit = [[N]*(N-1) for _ in range(r)]
    n = 0
    for i in range(N):
        if rabbits & 1<<i:
            rabbit[n][0] = N-i-1
            for j in range(N-2):
                if rabbit[n][j] == 0: rabbit[n][j+1] = 1
                elif rabbit[n][j] >= N-2-j: rabbit[n][j+1] = rabbit[n][j]-1
                elif board[rabbit[n][j]] == "W": rabbit[n][j+1] = rabbit[n][j]-1
                elif board[rabbit[n][j]] == "B": rabbit[n][j+1] = rabbit[n][j]+1
                else:
                    if j > 0: rabbit[n][j+1] = rabbit[n][j-1]
                    else: rabbit[n][j+1] = rabbit[n][j]-1
            n += 1
    for i in range(1,N-1):
        for j in range(n):
            if rabbit[j][i] < 0: continue
            flag = False
            for k in range(j+1,n):
                if rabbit[j][i] == rabbit[k][i]:
                    flag = True
                    for t in range(i,N-1):
                        rabbit[k][t] = -1
                if flag:
                    for t in range(i,N-1):
                        rabbit[j][t] = -1
    ret = 0
    for i in range(r):
        if 0<=rabbit[i][-1]<=1: ret += 1
    return ret

def bt(d, i, m):
    if d == r:
        return simulate(m)
    ret = 0
    b = 1 << (N-i)
    for j in range(N-i-r+d+1):
        b >>= 1
        ret += bt(d+1, i+j+1, m|b)
    return ret

comb = 1
for i in range(N, N-r,-1): comb *= i
for i in range(1,r+1): comb //= i
pos = bt(0, 0, 0)
print(pos/comb)