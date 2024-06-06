#1644: 소수의 연속합
import sys
input = sys.stdin.readline
N = int(input())
sieve = [1] * (N + 1)
sieve[0] = 0
sieve[1] = 0
prime = []
for i in range(2,N+1):
    if sieve[i]:
        prime.append(i)
        for j in range(i**2,N+1,i):
            sieve[j] = 0
count = 0
tail = 0
sum = 0
for k in prime:
    sum += k
    while N < sum:
        sum -= prime[tail]
        tail += 1
    if sum == N:
        count += 1
print(count)