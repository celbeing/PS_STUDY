#29197: 아침 태권도
import sys
input = sys.stdin.readline
N = int(input())

def euc(a,b):
    while b:
        a,b = b,a%b
    return a

ysh = set()
for _ in range(N):
    x,y = map(int,input().split())
    k = abs(euc(x,y))
    ysh.add((x//k,y//k))
print(len(ysh))