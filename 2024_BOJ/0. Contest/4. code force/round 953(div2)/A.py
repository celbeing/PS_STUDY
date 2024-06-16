import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = a[-1]
    b = sorted(a[:-1])
    result += b[-1]
    print(result)