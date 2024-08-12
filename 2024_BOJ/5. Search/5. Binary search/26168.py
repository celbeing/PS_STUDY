# 26168: 배열 전체 탐색하기
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = sorted(list(map(int,input().split())))

def bs(k):
    s,e = 0,n
    while s < e-1:
        m = (s+e)//2
        if A[m] >= k:
            e = m
        else:
            s = m+1
    if s < n and A[s] < k:
        return s+1
    else:
        return s

for _ in range(m):
    q = list(map(int,input().split()))
    res = 0
    if q[0] == 1:
        res = n-bs(q[1])
    elif q[0] == 2:
        res = n-bs(q[1]+1)
    else:
        res = bs(q[2]+1)-bs(q[1])
    print(res)