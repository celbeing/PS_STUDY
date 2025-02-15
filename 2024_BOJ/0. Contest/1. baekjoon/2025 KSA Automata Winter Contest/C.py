import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    y = set()
    result = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if b in y:
            continue
        else:
            result += 3
            result += len(y) * 2
            y.add(b)
    print(result)
solution()