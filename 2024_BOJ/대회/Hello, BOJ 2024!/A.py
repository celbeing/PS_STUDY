#A: 모바일 광고 입찰
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
count = 0
result = []
for _ in range(N):
    a,b = map(int,input().split())
    if a >= b:
        count += 1
    else:
        result.append(b-a)
result.sort()
if count >= K:
    print(0)
else:
    print(result[K-count-1])