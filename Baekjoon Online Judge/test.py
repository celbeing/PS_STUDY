from collections import deque
a, k = map(int, input().split())
bfs = deque([(a, 0)])
check = set()
check.add(a)
while bfs:
    now, count = bfs.popleft()
    if now == k:
        print(count)
        break

    if not(now + 1 in check):
        bfs.append((now + 1, count + 1))
        check.add(now + 1)
    if not(now << 1 in check) and now << 1 <= k:
        bfs.append((now << 1, count + 1))
        check.add(now << 1)