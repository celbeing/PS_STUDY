import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
Q = int(input())
s = list(map(int,input().split()))
size = [0]*(N+1)
now = 0
for i in range(1,N+1):
    while i-now > a[now]: now += 1
    size[i] = now+1
hole = []
for t in s:
    hole.append(size[t])
print(*hole)