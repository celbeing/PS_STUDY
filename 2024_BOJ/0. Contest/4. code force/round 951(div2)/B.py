import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    xor = x^y
    k = 1
    while True:
        if xor & k: break
        k <<= 1
    print(k)