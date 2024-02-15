#1991: 트리 순회
import sys
input = sys.stdin.readline
N = int(input())
tree = [[-1,-1] for _ in range(26)]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(N):
    node = list(input().split())
    parent = ord(node[0]) - 65
    left = ord(node[1]) - 65
    right = ord(node[2]) - 65
    tree[parent][0] = left
    tree[parent][1] = right
    pre = []
    ino = []
    pos = []
def traversal(p):
    if p >= 0:
        pre.append(alpha[p])
        traversal(tree[p][0])
        ino.append(alpha[p])
        traversal(tree[p][1])
        pos.append(alpha[p])
traversal(0)
print(''.join(pre))
print(''.join(ino))
print(''.join(pos))