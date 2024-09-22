#2186: 문자판
import sys
input = sys.stdin.readline
def solution():
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    N, M, K = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    word = list(input().rstrip())
    dp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == word[0]:
                dp[i][j] = 1
    for s in word[1:]:
        new_dp = [[0] * M for _ in range(N)]
        for x in range(N):
            for y in range(M):
                if board[x][y] == s:
                    for i in range(4):
                        for j in range(1, K + 1):
                            dx = x + d[i][0] * j
                            dy = y + d[i][1] * j
                            if 0 <= dx < N and 0 <= dy < M:
                                new_dp[x][y] += dp[dx][dy]
        dp = [new_dp[i][:] for i in range(N)]
    res = 0
    for i in range(N):
        res += sum(dp[i])
    print(res)
solution()