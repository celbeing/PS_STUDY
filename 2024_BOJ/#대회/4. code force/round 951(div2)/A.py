import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = int(1e9)
    for i in range(n-1):
        k = min(k,max(a[i],a[i+1]))
    print(k-1)