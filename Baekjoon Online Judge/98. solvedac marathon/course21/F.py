#10396: Black and white stones
import sys
input = sys.stdin.readline
def solution():
    A, B = map(int, input().split())
    B = A - B
    limit = A // B
    stone = list(input().strip())
    f, b = 0, len(stone) - 1
    res = 0
    while f < b:
        while f < len(stone) and stone[f] == 'B': f += 1
        while stone[b] == 'W': b -= 1
        if f >= b: break
        if b - f > limit: res += A
        else: res += B * (b - f)
        f += 1
        b -= 1
    print(res)
solution()