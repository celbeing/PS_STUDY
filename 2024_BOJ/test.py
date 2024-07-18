import sys
input = sys.stdin.readline
fib = [0]*10001
fib[1] = 1
fib[2] = 1
for i in range(3,10001):
    fib[i] = fib[i-1]+fib[i-2]
for i in range(1,int(input())+1):
    P,Q = map(int,input().split())
    print("Case #{}: {}".format(i,fib[P]%Q))