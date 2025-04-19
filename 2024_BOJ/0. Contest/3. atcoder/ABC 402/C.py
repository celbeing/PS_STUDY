import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    mat = [[] for _ in range(n + 1)]
    food = [0] * (m + 1)
    day = [0] * (n + 1)
    for i in range(1, m + 1):
        k = list(map(int, input().split()))
        for j in range(1, k[0] + 1):
            mat[k[j]].append(i)
    b = list(map(int, input().split()))
    for i in range(n):
        for t in mat[b[i]]:
            food[t] = i + 1
    for i in range(1, m + 1):
        day[food[i]] += 1
    food.sort()
    count = 0
    idx = 1
    for i in range(1, n + 1):
        while idx <= m and food[idx] == i:
            count += 1
            idx += 1
        print(count)
solution()