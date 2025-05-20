#12852: 1로 만들기 2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque([N])
check = dict()
tree = dict()
check[N] = 0

while q:
    k = q.popleft()
    if k == 1:
        break

    if k%3 == 0 and not(k//3 in check):
        q.append(k//3)
        check[k//3] = check[k]+1
        tree[k//3] = k
    if k%2 == 0 and not(k//2 in check):
        q.append(k//2)
        check[k//2] = check[k]+1
        tree[k//2] = k
    if not(k-1 in check):
        q.append(k-1)
        check[k-1] = check[k]+1
        tree[k-1] = k
route = [1]
while route[-1] != N:
    route.append(tree[route[-1]])
route.reverse()

print(check[1])
print(*route)