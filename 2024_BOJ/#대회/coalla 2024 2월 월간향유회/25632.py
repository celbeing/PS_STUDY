#25632: 소수 부르기 게임
import sys
input = sys.stdin.readline

A,B = map(int,input().split())
C,D = map(int,input().split())
yt,yj,both = 0,0,0

sieve = [True for _ in range(1001)]
sieve[0] = False
sieve[1] = False
prime = []
for i in range(2, 1001):
    if sieve[i]:
        prime.append(i)
        if A<=i<=B:
            yt += 1
            if C<=i<=D:
                both += 1
        if C<=i<=D:
            yj += 1

        for j in range(i**2,1001,i):
            if sieve[j]:
                sieve[j] = False

ytwin = True
if both % 2 == 0:
    if yt <= yj:
        ytwin = False
else:
    if yt < yj:
        ytwin = False

if ytwin:
    print("yt")
else:
    print("yj")