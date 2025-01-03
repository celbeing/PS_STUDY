import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    elder = max(a)
    junior = min(a)
    for k in a:
        print(max(elder - k, k - junior))
solution()