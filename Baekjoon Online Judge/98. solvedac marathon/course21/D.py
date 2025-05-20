#1516: 게임 개발
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N = int(input())
    requ = [[] for _ in range(N + 1)]
    deve = [[] for _ in range(N + 1)]
    time = [0] * (N + 1)
    built = [0] * (N + 1)
    t_sort = deque()
    income = [0] * (N + 1)
    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        time[i] = data[0]
        for j in range(1, len(data) - 1):
            requ[i].append(data[j])
            deve[data[j]].append(i)
            income[i] += 1
        if income[i] == 0:
            t_sort.append(i)
    while t_sort:
        now = t_sort.popleft()
        built[now] += time[now]
        for next in deve[now]:
            income[next] -= 1
            if income[next] == 0:
                t_sort.append(next)
            if built[next] < built[now]:
                built[next] = built[now]
    for i in range(1, N + 1):
        print(built[i])
solution()