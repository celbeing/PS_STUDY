import sys
input = sys.stdin.readline
n,m = map(int,input().split())
if n*m&1:
    print(n*m-1)
    print(1,1)
    for i in range(1,m-2,2):
        for j in range(2,n+1):
            print(j,i)
        for j in range(n,1,-1):
            print(j,i+1)
    for i in range(2,n+1):
        print(i,m-2)
    print(n,m-1)
    for i in range(n-1,1,-2):
        print(i,m-1)
        print(i,m)
        print(i-1,m)
        print(i-1,m-1)
    for i in range(m-2,1,-1):
        print(1,i)
else:
    print(n*m)
    if n&1:
        print(1,1)
        for i in range(1,m+1,2):
            for j in range(2,n+1):
                print(j,i)
            for j in range(n,1,-1):
                print(j,i+1)
        for i in range(m,1,-1):
            print(1,i)
    else:
        for i in range(1,n+1):
            print(i,1)
        for i in range(n,0,-2):
            for j in range(2,m+1):
                print(i,j)
            for j in range(m,1,-1):
                print(i-1,j)