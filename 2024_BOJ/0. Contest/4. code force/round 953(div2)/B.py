import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    k = b-a
    if k < 0: k = 0
    result = a*n + k*(k+1)//2
    if k > n: result -= (k-n)*(k-n+1)//2
    print(result)