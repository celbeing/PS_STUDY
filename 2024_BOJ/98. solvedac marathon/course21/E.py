#2737: 연속 합
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        N = int(input())
        cnt = 0
        for i in range(2, int((N * 2 + 0.25)**0.5 - 0.5)+1):
            cnt += 0 if (N - (i * (i + 1)) // 2) % i else 1
        print(cnt)
solution()