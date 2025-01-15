# 5398: 틀렸습니다
import sys
input = sys.stdin.readline
def solution():
    v, h = map(int, input().split())
    link = [[] for _ in range(v)]
    vert = dict()

    for i in range(v):
        x, y, w = map(str, input().split())
        x, y = int(x), int(y)
        for j in range(len(w)):
            vert[(x + j, y)] = (w[j], i)

    for i in range(h):
        x, y, w = map(str, input().split())
        x, y = int(x), int(y)
        for j in range(len(w)):
            if (x, y + j) in vert and vert[(x, y + j)][0] != w[j]:
                link[vert[(x, y + j)][1]].append(i)

    def match(k):
        if visit[k]: return False
        visit[k] = 1
        for t in link[k]:
            if v_h[t] == -1:
                v_h[t] = k
                return True
        for t in link[k]:
            if v_h[t] >= 0 and match(v_h[t]):
                v_h[t] = k
                return True
        return False

    v_h = [-1] * h
    count = 0

    for i in range(v):
        visit = [0] * v
        if match(i): count += 1

    print(v + h - count)
for _ in range(int(input())): solution()