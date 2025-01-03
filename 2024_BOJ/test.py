import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for i in range(t):
        if i: print()
        n = list(map(int, input().split()))
        print(*n)
        if 17 in n and 18 in n:
            print("both")
        elif 17 in n:
            print("zack")
        elif 18 in n:
            print("mack")
        else:
            print("none")
solution()