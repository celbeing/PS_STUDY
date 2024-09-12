#10971: 외판원 순회 2
import sys
input = sys.stdin.readline

def bt(n, route, cost, record, matrix):
    if len(route) == n:
        if matrix[route[-1]][route[0]]:
            return cost + matrix[route[-1]][route[0]]
        else: return int(1e9)
    for i in range(n):
        if i in route or (route and matrix[route[-1]][i] == 0): continue
        if cost + matrix[route[-1]][i] > record: continue
        record = min(record, bt(n, route + [i], cost + matrix[route[-1]][i], record, matrix))
    return record

def solution():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    record = int(1e9)
    for i in range(N):
        record = min(record, bt(N, [i], 0, int(1e9), cost))
    print(record)
solution()