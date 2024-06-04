import sys
from math import log2
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
K = int(input())

def decode(a):
    if a < 2: return (-1,-1)
    j = int(log2(a))
    i = 0
    if a == 2**j:
        j -= 1
        i = j
    else:
        i = int(log2(a-2**j))
    if 2**i+2**j == a:
        return (i,j)
    else:
        return (-1,-1)

key = [i for i in range(8)]
for a in A:
    i,j = decode(a)
    t = key[i]
    key[i] = key[j]
    key[j]= t
print(key[K])