# 14398: 피타고라스 수
import sys
from math import gcd
input = sys.stdin.readline
def solution():
    n = int(input())
    stick = list(map(int, input().split()))
    odd = []
    even = []
    for s in stick:
        if s & 1:
            odd.append(s)
        else:
            even.append(s)
    count = 0
    graph = [[] for _ in range(len(odd))]
    pyt = [-1] * len(even)
    for i in range(len(odd)):
        for j in range(len(even)):
            c = int((odd[i] ** 2 + even[j] ** 2) ** 0.5)
            if  gcd(odd[i], gcd(even[j], c)) == 1 and odd[i] ** 2 + even[j] ** 2 == c ** 2:
                graph[i].append(j)

    def match(k):
        if visit[k]: return False
        visit[k] = True
        if len(graph[k]) == 0: return False
        for t in graph[k]:
            if pyt[t] == -1:
                pyt[t] = k
                return True
        for t in graph[k]:
            if pyt[t] >= 0 and match(pyt[t]):
                pyt[t] = k
                return True
        return False

    for i in range(len(odd)):
        visit = [False] * len(odd)
        if match(i): count += 1

    print(count)
solution()