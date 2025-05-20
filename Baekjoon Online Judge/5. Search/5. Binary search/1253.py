# 1253: 좋다
import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int,input().split())))
count = 0

def bin(s,e,t):
    while s < e:
        m = (s+e)//2
        if A[m] < t:
            s = m+1
        elif A[m] > t:
            e = m
        else:
            while m >= 0 and A[m] == t: m -= 1
            return m+1
    return -1

for i in range(N):
    for j in range(N):
        if i == j: continue
        t = A[i]-A[j]
        if t < A[0] or t > A[-1]: continue

        if bin(0,min(i,j),t) >= 0:
            count += 1
            break
        if bin(min(i,j)+1,max(i,j),t) >= 0:
            count += 1
            break
        if bin(max(i,j)+1,N,t) >= 0:
            count += 1
            break

print(count)