# 9623: 부분 수열의 길이
import sys
input = sys.stdin.readline
def solution():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        pre = []
        sum = 0
        pre.append((0,0))
        for i in range(n):
            sum += arr[i]
            pre.append((sum, i + 1))
        pre.sort(reverse = True)
        for check in range(0, n + 1):
            u = pre[check][0] + x