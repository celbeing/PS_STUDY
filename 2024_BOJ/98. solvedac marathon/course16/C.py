#9079: 동전 게임
import sys
input = sys.stdin.readline
def check(k):
    count = 0
    coins = [0] * 9
    if k & 1:
        count += 1
        for i in range(0, 9, 3):
            coins[i] = 0 if coins[i] else 1
    if k & 2:
        count += 1
        for i in range(1, 9, 3):
            coins[i] = 0 if coins[i] else 1
    if k & 4:
        count += 1
        for i in range(2, 9, 3):
            coins[i] = 0 if coins[i] else 1
    if k & 8:
        count += 1
        for i in range(3):
            coins[i] = 0 if coins[i] else 1
    if k & 16:
        count += 1
        for i in range(3, 6):
            coins[i] = 0 if coins[i] else 1
    if k & 32:
        count += 1
        for i in range(6, 9):
            coins[i] = 0 if coins[i] else 1
    if k & 64:
        count += 1
        for i in range(0, 9, 4):
            coins[i] = 0 if coins[i] else 1
    if k & 128:
        count += 1
        for i in range(2, 8, 2):
            coins[i] = 0 if coins[i] else 1
    return coins, count

def solution():
    for _ in range(int(input())):
        h, t = [0] * 9, [0] * 9
        for i in range(3):
            x, y, z = map(str, input().split())
            h[i * 3] = 1 if x == 'H' else 0
            h[i * 3 + 1] = 1 if y == 'H' else 0
            h[i * 3 + 2] = 1 if z == 'H' else 0
        for i in range(9):
            t[i] = 0 if h[i] else 1

        rec = 9
        for i in range(256):
            res, count = check(i)
            if (res == h or res == t) and rec > count:
                rec = count
        print(rec if rec < 9 else -1)

solution()