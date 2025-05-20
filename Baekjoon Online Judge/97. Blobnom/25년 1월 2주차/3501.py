# 3501: 최대공약수 맞추기 게임
import sys
input = sys.stdin.readline
def solution():
    n = int(input().strip())
    p = [0] * (n + 1)
    prime = []
    for i in range(2, n + 1):
        if p[i] == 0:
            prime.append(i)
            for j in range(i ** 2, n + 1, i):
                p[j] = 1

    i, j = 0, len(prime) - 1
    cnt = 0

    while i <= j:
        x = prime[j]
        j -= 1
        if i <= j and prime[i] <= n // x:
            i += 1
        cnt += 1
    print(cnt)
solution()