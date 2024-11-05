#30705: ENDLESS RAIN
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    linked = [i for i in range(N + 1)]
    parasol = 0
    day = 0
    for _ in range(M):
        day += 1
        need = 0
        a, b = map(int, input().split())
        while a < b:
            while linked[a] > a:
                k = linked[a]
                linked[a] = max(linked[a], b)
                a = k
            if a < b:
                need += 1
                linked[a] = b
                a += 1
        if need <= day:
            day -= need
        else:
            parasol += need - day
            day = 0
    print(parasol)
solution()