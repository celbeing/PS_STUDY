# 26600: map, filter
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    l = 0
    now = a[0]
    picker = {0: now}
    count = [1]
    for i in range(1, n):
        if a[i] == now:
            count[l] += 1
        else:
            l += 1
            picker[l] = a[i]
            now = a[i]
            count.append(1)
    for _ in range(int(input())):
        query = map(str, input().split())
        if query[0] == 'map':
            