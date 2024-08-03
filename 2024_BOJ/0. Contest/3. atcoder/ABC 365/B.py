import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
num = dict()
for i in range(N):
    num[A[i]] = i+1
A.sort()
print(num[A[-2]])