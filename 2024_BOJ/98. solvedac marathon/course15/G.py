#23061: 백남이의 여행 준비
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    dp = [0] * 1000001
    for _ in range(N):
        W, V = map(int, input().split())
        for i in range(1000000, W - 1, -1):
            if dp[i] < dp[i - W] + V:
                dp[i] = dp[i - W] + V
    high = 0
    result = 0
    for i in range(M):
        bag = int(input())
        k = dp[bag] / bag
        if k > high:
            result = i
            high = k
    print(result + 1)
solution()