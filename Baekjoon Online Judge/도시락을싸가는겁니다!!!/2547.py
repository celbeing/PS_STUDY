# 2547: 사탕 선생 고창영
import sys
input = sys.stdin.readline
def solution():
    input()
    n = int(input())
    s = sum([int(input()) for _ in range(n)])
    print('NO' if s % n else 'YES')
for _ in range(int(input())):
    solution()