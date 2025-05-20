# 1365: 꼬인 전깃줄
import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
lis = [0]

def bin(k):
    s,e = 0,len(lis)
    while s < e:
        m = (s+e)//2
        if lis[m] < k: s = m+1
        else: e = m
    return s

for l in L:
    if lis[-1] < l: lis.append(l)
    else: lis[bin(l)] = l
print(N-len(lis)+1)