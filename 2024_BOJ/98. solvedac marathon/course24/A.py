#8721: Wykreślanka
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    num = 1
    for N in arr:
        if N == num: num += 1
        else: count += 1
    print(count)
solution()