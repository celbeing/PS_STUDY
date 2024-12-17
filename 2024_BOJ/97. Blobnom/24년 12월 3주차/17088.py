# 17088: 등차수열 변환
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    b = list(map(int, input().split()))
    if n == 1:
        print(0)
        return 0
    D = b[1] - b[0]
    S = b[0]
    result = n + 1
    for i in range(-1, 2):
        for j in range(-i - 1, -i + 2):
            d = D + j
            count = 0
            now = S + i
            for c in b:
                k = abs(now - c)
                if k == 1: count += 1
                elif k > 1: break
                now += d
            else:
                result = min(result, count)
    if result == n + 1: result = -1
    print(result)
solution()