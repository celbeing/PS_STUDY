# 8659: Samochody
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    car = list(map(int, input().split())) + [0]
    total = 0
    right = 0
    left = 0
    for c in car:
        if c == 1: right += 1
        else:
            total += left * right
            right = 0
            left += 1
    print(total)
solution()