import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    taro = [1] * (N + 1)
    for _ in range(M):
        a, b = map(str, input().split())
        a = int(a)
        if taro[a] and b == "M":
            taro[a] = 0
            print("Yes")
        else:
            print("No")
solution()