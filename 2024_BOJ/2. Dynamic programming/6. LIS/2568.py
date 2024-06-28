# 2568: 전깃줄 - 2
import sys
input = sys.stdin.readline
N = int(input())
line = [tuple(map(int, input().split())) for _ in range(N)]
line.sort()
T = dict()

def bin(k):
    s,e = 0,len(lis)
    while s<e:
        m = (s+e)//2
        if lis[m] < k: s = m+1
        else: e = m
    return s

lis = [0]

for a,b in line:
    if lis[-1] < b:
        T[b] = lis[-1]
        lis.append(b)
    else:
        k = bin(b)
        lis[k] = b
        T[b] = lis[k-1]

k = lis[-1]
stack = []
while k > 0:
    stack.append(k)
    k = T[k]

print(N-len(lis)+1)
for a,b in line:
    if stack and stack[-1] == b:
        stack.pop()
    else:
        print(a)