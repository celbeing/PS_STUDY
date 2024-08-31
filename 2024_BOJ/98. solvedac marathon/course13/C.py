#10434: 행복한 소수
import sys
input = sys.stdin.readline

def happy(m):
    path = dict()
    a = m
    while True:
        k = 0
        b = a
        while b > 0:
            k += (b%10)**2
            b //= 10
        if k in path: return False
        elif k == 1: return True
        path[a] = k
        a = k

sieve = [1]*10001
sieve[0] = sieve[1] = 0
for i in range(2,10001):
    if sieve[i]:
        for j in range(i**2,10001,i):
            sieve[j] = 0

for _ in range(int(input())):
    t,m = map(int,input().split())
    if sieve[m] and happy(m):
        print(t,m,"YES")
    else:
        print(t,m,"NO")