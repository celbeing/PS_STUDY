# 23317: 구슬 굴리기
import sys
input = sys.stdin.readline
dp = [[0] * 31 for _ in range(31)]
dp[0][0] = 1
for i in range(30):
    for j in range(30):
        dp[i][j + 1] += dp[i][j]
        dp[i + 1][j] += dp[i][j]

n = int(input())
m = int(input())
res = 1
cp = [tuple(map(int, input().split())) for _ in range(m)]
cp.sort()
x, y = 0, 0
for nx, ny in cp:
    nx -= ny
    tx = nx - x
    ty = ny - y
    if tx < 0 or ty < 0:
        res = 0
        break
    else:
        res *= dp[tx][ty]
        x, y = nx, ny
bottom = 0
for i in range(n - x - y):
    bottom += dp[n - x - y - 1 - i][i]
print(res * bottom)