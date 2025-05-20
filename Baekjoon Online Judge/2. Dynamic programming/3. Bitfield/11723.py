#11723: 집합
import sys
input = sys.stdin.readline
M = int(input())
S = 0b0
for _ in range(M):
    order = list(input().split())
    if order[0] == "add":
        S = S | (0b1 << int(order[1]))
    elif order[0] == "remove":
        S = S & ~(0b1 << int(order[1]))
    elif order[0] == "check":
        if S & (0b1 << int(order[1])):
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        S = S ^ (0b1 << int(order[1]))
    elif order[0] == "all":
        S = 0b111_111_111_111_111_111_111
    else:
        S = 0b0