#31718: Double Up
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
d = dict()
k = 0
for a in A:
    while (a ^ 1) & 1:
        a >>= 1
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

    if k < d[a]:
        k = d[a]
print(k)