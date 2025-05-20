# 20442: ㅋㅋ루ㅋㅋ
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    a = list(input().strip())
    s, e = 0, len(a) - 1
    r = deque()
    while s <= e:
        count = 0
        while s <= e and a[s] == 'R':
            count += 1
            s += 1
        s += 1
        while e >= s and a[e] == 'R':
            count += 1
            e -= 1
        e -= 1
        r.append(count)
    result = 0
    sumR = 0
    while r:
        sumR += r.pop()
        if sumR == 0: continue
        result = max(result, sumR + len(r) * 2)
    print(result)
solution()