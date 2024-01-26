#14003: 가장 긴 증가하는 부분 수열 5
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)

def binarysearch(k,B):
    s = 0
    e = len(B)
    while s < e:
        m = (s+e)//2
        if B[m] < k:
            s = m+1
        elif B[m] > k:
            e = m
        else:
            return m
    return s

B = [-1e10]
I = [0]
lis = [0] * (N+1)
pointer = [0] * (N+1)
peek = 0

for i in range(1,N+1):
    t = binarysearch(A[i],B)
    if t == len(B):
        B.append(A[i])
        I.append(i)
        pointer[i] = I[t-1]
        lis[i] = t
    else:
        B[t] = A[i]
        I[t] = i
        pointer[i] = I[t-1]
        lis[i] = t
    if t > lis[peek]:
        peek = i

print(lis[peek])
array = []
while peek > 0:
    array.append(A[peek])
    peek = pointer[peek]
print(*reversed(array))