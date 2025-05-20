# 2957: 이진 탐색 트리
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    tree = [[0,0,0] for _ in range(N + 1)]
    count = 0
    tree[1][0] = int(input())
    print(count)
    i = 2
    for _ in range(N - 1):
        k = int(input())
        t = 1
        while True:
            if tree[t][0] > k:
                if tree[t][1] == 0:
                    tree[t][1] = i
                    tree[i][0] = k
                    i += 1
                    break
                else:
                    t = tree[t][1]
            elif tree[t]
solution()