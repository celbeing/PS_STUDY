#14002: 가장 긴 증가하는 부분 수열 4
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
recent = []
lis = [0] * 1000
lis[0] = A[0]
peek = 1

def binary(arr, e, k):
    s = 0
    while s < e:
        m = (s+e)//2
        if arr[m] < k:
            s = m+1
        else:
            e = m
    return e

index = 1
for i in range(1,N):
    t = binary(lis, peek, A[i])
    lis[t] = A[i]

    if peek < t:
        peek = t
        recent.clear()
        for j in range(t):
            recent.append(lis[j])

print(peek)
print(*recent)