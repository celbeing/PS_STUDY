#13325: 이진 트리
import sys
input = sys.stdin.readline
k = int(input())
w = list(map(int,input().split()))
n = len(w)-4
res = sum(w[-(1<<k):])
while n>=0:
    l,r = w.pop(),w.pop()
    res += abs(l-r)
    res += w[n//2]
    w[n//2] += max(l,r)
    n -= 2
print(res + abs(w[0]-w[1]))