# 2721: 삼각수의 합
import sys
input = sys.stdin.readline
def solution():
    tri = [0] * 302
    for i in range(1, 302):
        tri[i] += i + tri[i - 1]
    w = [0] * 301
    for i in range(1, 301):
        w[i] = w[i - 1] + i * tri[i + 1]
    for _ in range(int(input())):
        print(w[int(input())])
solution()