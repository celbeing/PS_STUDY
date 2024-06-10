import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = sorted(a[:])
    s = b[1]
    k = -1
    for i in range(n):
        if s == a[i]:
            k = i
            break
    if b[0] == b[-1]:
        print("NO")
    else:
        print("YES")
        print("RB"+"R"*(n-2))