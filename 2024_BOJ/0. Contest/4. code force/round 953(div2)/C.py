import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    limit = (n//2)*(n//2+1)*4
    if not(n&1): limit -= n//2
    result = [i for i in range(1,n+1)]

    if k > limit or k&1: print("No")
    else:
        k //= 2
        s,e = 1,n
        while k and s < e:
            if k >= e-s:
                tmp = result[s-1]
                result[s-1] = result[e-1]
                result[e-1] = tmp
                k -= e-s
                e -= 1
                s += 1
            else:
                e -= 1
        if k: print("No")
        else:
            print("Yes")
            print(*result)