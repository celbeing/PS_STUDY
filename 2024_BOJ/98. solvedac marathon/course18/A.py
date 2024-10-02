#10163: 색종이
import sys
input = sys.stdin.readline
def solution():
    ground = [[0] * 1001 for _ in range(1001)]
    N = int(input())
    for i in range(1, N + 1):
        a, b, c, d = map(int, input().split())
        for x in range(a, a + c):
            for y in range(b, b + d):
                ground[x][y] = i
    paper = [0] * (N + 1)
    for i in range(1001):
        for j in range(1001):
            paper[ground[i][j]] += 1
    for n in range(1, N + 1):
        print(paper[n])
solution()