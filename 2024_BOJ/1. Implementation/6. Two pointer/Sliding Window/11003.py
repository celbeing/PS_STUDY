#11003: 최솟값 찾기
import sys
from collections import deque
input = sys.stdin.readline
N,L = map(int,input().split())
A = list(map(int,input().split()))
window = deque()
result = [0]*N

for i in range(N):
    if window and window[0][1] < i-L+1:
        window.popleft()
    while len(window) > 0 and A[i] < window[-1][0]:
        window.pop()
    window.append((A[i],i))
    result[i] = window[0][0]
print(*result)