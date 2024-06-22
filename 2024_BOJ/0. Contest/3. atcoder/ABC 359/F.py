import sys
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int,input().split())))
d = [1]*N
result = 0
for i in range(1,N):
    for j in range(i):
        if d[j]*A[j] <= d[j+1]*A[j+1]:
            result += d[i]*A[i]+d[j]*A[j]
            d[j] += 2
            d[i] += 2
            break
print(result)