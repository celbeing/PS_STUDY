#6588: 골드바흐의 추측
import sys
input = sys.stdin.readline

sieve = [True] * 1_000_001
sieve[0] = False
sieve[1] = False
prime = []
for i in range(2, 1_000_001):
    if sieve[i]:
        for j in range(i**2, 1_000_001, i):
            if sieve[j]:
                sieve[j] = False
        prime.append(i)
del prime[0]

while True:
    n = int(input())
    if n == 0:
        break
    for a in prime:
        if sieve[n - a]:
            print("{} = {} + {}".format(n,a,n-a))
            break
        if a > n//2:
            print("Goldhach's conjucture is wrong.")
            break