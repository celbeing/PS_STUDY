import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n = int(input())
        print('YES')
        a = [i for i in range(1, n + 1)]
        print(*a)
solution()