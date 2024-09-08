import sys
input = sys.stdin.readline
H,W,Q = map(int,input().split())
wall = H*W
grid = [[1]*(W+1) for _ in range(H+1)]
for _ in range(Q):
    r,c = map(int,input().split())
    if grid[r][c]:
        wall -= 1
        grid[r][c] = 0
    else:
        for i in range(r+1, H+1):
            if grid[i][c]:
                wall -= 1
                grid[i][c] = 0
                break
        for i in range(c+1, W+1):
            if grid[r][i]:
                wall -= 1
                grid[r][i] = 0
                break
        for i in range(r-1, 0, -1):
            if grid[i][c]:
                wall -= 1
                grid[i][c] = 0
                break
        for i in range(c-1, 0, -1):
            if grid[r][i]:
                wall -= 1
                grid[r][i] = 0
                break
print(wall)