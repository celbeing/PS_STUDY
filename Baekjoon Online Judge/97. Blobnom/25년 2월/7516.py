# 7516: 알렉산드리아의 디오판토스
import sys
input = sys.stdin.readline
def solution():
    prime = []
    sieve = [1] * 31623
    for i in range(2, 31623):
        if sieve[i]:
            prime.append(i)
            for j in range(i * i, 31623, i):
                sieve[j] = 0

    for t in range(int(input())):
        res = 1
        n = int(input())
        idx = 0
        while idx < 3401 and n > 1:
            count = 0
            while n % prime[idx] == 0:
                count += 1
                n //= prime[idx]
            idx += 1
            res *= (count * 2) + 1
        if n > 1:
            res *= 3
        res >>= 1
        res += 1

        if t: print()
        print(f'Scenario #{t + 1}:')
        print(res)
solution()