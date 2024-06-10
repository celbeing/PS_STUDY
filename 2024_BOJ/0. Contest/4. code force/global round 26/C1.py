import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    large = abs(a[0])
    small = a[0]
    for i in range(1,n):
        l,s = 0,0
        if a[i] == 0: continue
        elif a[i] > 0:
            l = large+a[i]
            s = small+a[i]
        else:
            l = max(large+a[i],abs(small+a[i]))
            s = small+a[i]
        large = l
        small = s
    print(max(large,abs(small)))