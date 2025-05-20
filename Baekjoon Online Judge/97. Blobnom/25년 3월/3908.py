# 3908: 서로 다른 소수의 합
import sys
input = sys.stdin.readline
def solution():
    prime = []
    sieve = [1] * 1120
    for i in range(2, 1120):
        if sieve[i]:
            prime.append(i)
            for j in range(i * i, 1120, i):
                sieve[j] = 0
    goldbach = [[0] * 1121 for _ in range(15)]
    goldbach[0][0] = 1
    for p in prime:
        for i in range(13, -1, -1):
            for j in range(1120, -1, -1):
                if goldbach[i][j] and j + p < 1121:
                    goldbach[i + 1][j + p] += goldbach[i][j]
    for _ in range(int(input())):
        n, k = map(int, input().split())
        print(goldbach[k][n])
solution()