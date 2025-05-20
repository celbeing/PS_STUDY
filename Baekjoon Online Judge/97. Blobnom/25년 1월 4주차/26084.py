# 26084: DPS
import sys
input = sys.stdin.readline
def solution():
    team = input().rstrip()
    dup = set()
    dup.update(list(team))
    count = dict()
    for _ in range(int(input())):
        handle = input().rstrip()
        count[handle[0]] = count.get(handle[0], 0) + 1
    res = 1
    for k in team:
        count[k] = count.get(k, 0)
        res *= count[k]
        count[k] -= 1
        if count[k] < 0: count[k] = 0
    if len(dup) == 1:
        res //= 6
    elif len(dup) == 2:
        res //= 2
    print(res)
solution()