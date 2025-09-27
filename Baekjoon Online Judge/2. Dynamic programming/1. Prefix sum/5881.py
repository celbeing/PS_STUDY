# 5881: Bookshelf
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
dp = [float('inf')] * (n + 1)
dp[0] = 0
books = [(0, 0)]
for i in range(n):
    h, w = map(int, input().split())
    books.append((h, w + books[i][1]))

for i in range(1, n + 1):
    high = 0
    for j in range(i, 0, -1):
        s = books[i][1] - books[j - 1][1]
        if s > l: break
        if high < books[j][0]: high = books[j][0]
        dp[i] = min(dp[i], dp[j - 1] + high)

print(dp[-1])