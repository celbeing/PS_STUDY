#2737: 연속 합
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        N = int(input())
        cnt = 0
        k = 2
        while k * (k + 1) <= N * 2:
            t = N - (k * (k + 1)) // 2
            if t >= 0 and t % k == 0: cnt += 1
            k += 1
        print(cnt)
solution()