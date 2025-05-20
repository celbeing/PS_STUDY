#11025: 요세푸스 문제 3
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
res = 0
for i in range(1,N+1):
    res = (res+K)%i
print(res+1)