# 15786: Send me the money
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    rem = list(input().strip())
    for _ in range(m):
        post = list(input().strip())
        idx = 0
        for a in post:
            if a == rem[idx]:
                idx += 1
            if idx == n:
                print('true')
                break
        else:
            print('false')
solution()