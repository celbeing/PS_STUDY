import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,f,k = map(int,input().split())
    a = list(map(float,input().split()))
    a[f-1] -= 0.1
    fav = a[f-1]
    a.sort(reverse=True)
    cut = a[k-1]
    a = a[k:]
    if fav in a:
        if cut - 0.1 == fav: print("MAYBE")
        else: print("NO")
    else:
        print("YES")