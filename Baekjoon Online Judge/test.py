from heapq import heappush, heappop
hq = []
for _ in range(10):
    heappush(hq, int(input()))
print(hq)