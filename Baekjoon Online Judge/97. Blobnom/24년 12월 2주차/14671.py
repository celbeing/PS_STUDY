# 14671: 영정이의 청소
import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split())
    floor = [[0] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        x %= 2; y %= 2
        if floor[x][y]: continue
        for i in range(x, n, 2):
            for j in range(y, m, 2):
                if floor[i][j]: continue
                floor[i][j] = 1
                count += 1
                if count == n * m: return "YES"
    return "NO"
print(solution())