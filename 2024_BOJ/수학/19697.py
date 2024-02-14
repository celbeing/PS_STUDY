#19697: Island
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
road = [0 for _ in range(M)]
for _ in range(N+M-1):
    u,v = map(int,input().split())
    if u > N:
        road[u - N - 1] += 1
    if v > N:
        road[v - N - 1] += 1

counter = [0 for _ in range(200000)]
for a in road:
    for i in range(2, a):
        counter[i] += 1

for i in range(200000):
    if counter[i] > 0:
        print(*[i,counter[i]])