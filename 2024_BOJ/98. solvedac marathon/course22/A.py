#27325: 3つの箱
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    S = list(input().rstrip())
    ball = 1
    count = 0
    for s in S:
        if s == "L": ball -= 1
        else: ball += 1
        if ball == 0: ball += 1
        elif ball == 4: ball -= 1
        if ball == 3: count += 1
    print(count)
solution()