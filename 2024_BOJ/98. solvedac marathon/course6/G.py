import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int,input().split()))

def gcd(s,e):
    n = e-s
    if n == 0: return 0
    elif n == 1: return S[s]

    a = S[s]
    for i in range(1,n):
        b = S[s+i]
        while b > 0:
            a,b = b,a%b
    return a

def sc(s,e):
    if s == e: return 0
    elif e-s == 1: return S[s]
    m = (s+e)//2
    return max(gcd(s,m)+sc(m,e), sc(s,m)+gcd(m,e))

print(sc(0,N))