from collections import deque
n, q = map(int, input().split())
tower = deque([0] * n)
exist = set()
count = 0
for i in range(q):
    c = int(input())
    if c in exist:
        while tower[0] != c:
            tower.append(tower.popleft())
            count += 1
        tower[0] = 0
        exist.remove(c)
    else:
        while tower[0] != 0:
            tower.append(tower.popleft())
            count += 1
        tower[0] = c
        exist.add(c)
print(count)