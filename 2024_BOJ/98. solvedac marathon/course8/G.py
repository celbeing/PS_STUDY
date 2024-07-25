import sys
from collections import deque
input = sys.stdin.readline
hx = [-2,-2,-1,-1,1,1,2,2]
hy = [-1,1,-2,2,-2,2,-1,1]
mx = [-1,0,0,1]
my = [0,-1,1,0]
K = int(input())
W,H = map(int,input().split())
cage = [list(map(int,input().split())) for _ in range(H)]
kvst = [[-1]*W for _ in range(H)]
kvst[0][0] = K
bfs = deque([(K,0,0)])
step = 0
breadth = 1
while bfs:
    n_breadth = 0
    for _ in range(breadth):
        k,x,y = bfs.popleft()
        if x == H-1 and y == W-1:
            print(step)
            exit()
        if k:
            for d in range(8):
                dx = x+hx[d]
                dy = y+hy[d]
                if 0<=dx<H and 0<=dy<W and cage[dx][dy] == 0 and kvst[dx][dy] < k-1:
                    n_breadth += 1
                    kvst[dx][dy] = k-1
                    bfs.append((k-1,dx,dy))
        for d in range(4):
            dx = x+mx[d]
            dy = y+my[d]
            if 0<=dx<H and 0<=dy<W and cage[dx][dy] == 0 and kvst[dx][dy] < k:
                n_breadth += 1
                kvst[dx][dy] = k
                bfs.append((k,dx,dy))
    breadth = n_breadth
    step += 1
print(-1)