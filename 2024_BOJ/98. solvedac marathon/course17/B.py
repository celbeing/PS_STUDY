#14381: 숫자세는 양 (Small)
import sys
input = sys.stdin.readline
def solution():
    for i in range(1, int(input()) + 1):
        N = int(input())
        step = N
        sleep = set()
        if N == 0:
            print(f"Case #{i}: INSOMNIA")
        else:
            while len(sleep) < 10:
                k = 1
                while k <= N:
                    sleep.add((N % (k * 10)) // k)
                    k *= 10
                N += step
            print(f"Case #{i}: {N-step}")
solution()