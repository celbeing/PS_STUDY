#1991: 4. Tree 순회
import sys
input = sys.stdin.readline
N = int(input())
tree = [[-1,-1,-1] for _ in range(26)]
tree[0][0] = 0
for _ in range(N):
    node = list(input().split())
    print(node)
print(ord('.'))
print(ord('A'))