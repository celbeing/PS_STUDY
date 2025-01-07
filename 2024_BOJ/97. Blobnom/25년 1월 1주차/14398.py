# 14398: 피타고라스 수
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    stick = list(map(int, input().split()))
    pair = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            c = stick[i] ** 2 + stick[j] ** 2
            if c == int(c ** 0.5) ** 2:
                pair[i].append(j)
                pair[j].append(i)
    count = 0
    linked = [-1] * n
    current = [0] * n
    def match(k):
        for i in range(current[k], len(pair[k])):
            current[k] += 1
            if linked[pair[k][i]] == -1:
                linked[k] = pair[k][i]
                linked[pair[k][i]] = k
                return 1
            origin = linked[pair[k][i]]
            
            if match(pair[k][i]):
                linked[k] = pair[k][i]
                linked[pair[k][i]] = k
                return 1
        return 0
    for i in range(n):
        if linked[i] >= 0: continue
        count += match(i)
    print(count)
solution()