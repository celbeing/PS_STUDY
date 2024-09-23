#2854: 문제 출제
import sys
input = sys.stdin.readline
def solution():
    div = int(1e9 + 7)
    N = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    DP = [[0] * 2 for _ in range(N + 1)]
    DP[0][0] = 1
    for i in range(1, N + 1):
        DP[i - 1][1] = (DP[i - 2][0] + DP[i - 2][1]) * B[i - 1]
        DP[i - 1][1] %= div
        DP[i][0] = (DP[i - 1][0] + DP[i - 1][1]) * A[i]
        DP[i][0] += DP[i - 1][0] * B[i - 1]
        DP[i][0] += DP[i - 1][1] * (B[i - 1] - 1)
        DP[i][0] %= div
    print(DP[N][0])
solution()