#13247: 토끼의 이동
import sys
input = sys.stdin.readline
board = list(input().rstrip())
r = int(input())
N = len(board)

def simulate(rabbits):
    now = [0]*N
    for i in range(N):
        if rabbits & 1<<i:
            now[-i-1] = 1
    R = []
    for i in range(N-1, 1, -1):
        next = [0]*i


def bt(d, i, m):
    if d == r: return simulate(m)
    ret = 0
    b = 1 << (N-i)
    for j in range(N-i-r+d):
        b >>= 1
        ret += bt(d+1, i+j+1, m|b)
    return ret

comb = 1
for i in range(N, N-r,-1): comb *= i
for i in range(1,r+1): comb //= i
pos = bt(0, 0, 0)
print(pos/comb)