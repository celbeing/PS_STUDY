#15666: N과 M (12)
import sys
input = sys.stdin.readline
def recurs(n, m, k, r):
    result = []
    if len(r) == m:
        return [r[:]]
    for i in range(k, len(n)):
        r.append(n[i])
        result += recurs(n, m, i, r)
        r.pop()
    return result

def solution():
    N, M = map(int, input().split())
    num = sorted(list(set(map(int, input().split()))))
    result = recurs(num, M, 0, [])
    for r in result:
        print(*r)

solution()