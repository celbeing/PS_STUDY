import sys
input = sys.stdin.readline

t = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def bin_check():
    ret = 0
    t = 1
    for j in range(3, 6):
        if grid[0][j]: ret |= t
        t <<= 1
    for i in range(1, 4):
        for j in range(9):
            if grid[i][j]: ret |= t
            t <<= 1
    for j in range(3, 6):
        if grid[4][j]: ret |= t
        t <<= 1
    if ret in check:
        return 0
    else:
        check.add(ret)
        return 1

def dfs(count):
    ret = count
    for x, y in peg:
        for k in range(4):
            dx, dy = x + d[k][0], y + d[k][1]
            tx, ty = x + t[k][0], y + t[k][1]
            if 0 <= dx < 5 and 0 <= dy < 9 and grid[dx][dy] == 0:
                if grid[tx][ty] == 1:
                    grid[tx][ty] = 0
                    grid[x][y] = 0
                    grid[dx][dy] = 1
                    peg.remove((tx, ty))
                    peg.remove((x, y))
                    peg.add((dx, dy))
                    if bin_check(): ret = max(ret, dfs(count + 1))
                    grid[tx][ty] = 1
                    grid[x][y] = 1
                    grid[dx][dy] = 0
                    peg.add((tx, ty))
                    peg.add((x, y))
                    peg.remove((dx, dy))
    return ret

tc = int(input())
for n in range(tc):
    grid = [[0] * 9 for _ in range(5)]
    peg = set()
    check = set()
    peg_count = 0
    for i in range(5):
        line = list(input().strip())
        for j in range(9):
            if line[j] == '#':
                grid[i][j] = 2
            elif line[j] == 'o':
                grid[i][j] = 1
                peg.add((i, j))
                peg_count += 1

    ans = dfs(0)
    print(peg_count - ans, ans)
    if n + 1 == tc:
        break
    input()