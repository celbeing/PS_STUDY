#11447: Colby's Costly Collectibles
import sys
input = sys.stdin.readline
def solution():
    move = {"x": (2, 0), "y": (1, 1), "z": (-1, 1)}
    for _ in range(int(input())):
        result = 0
        dots = [(0, 0)]
        for _ in range(int(input())):
            d, l = map(str, input().split())
            x = dots[-1][0] + move[d][0] * int(l)
            y = dots[-1][1] + move[d][1] * int(l)
            dots.append((x, y))
        dots.append((0,0))
        for i in range(0, len(dots) - 1):
            result += dots[i][0] * dots[i + 1][1] - dots[i][1] * dots[i + 1][0]
        print(abs(result // 2))
solution()