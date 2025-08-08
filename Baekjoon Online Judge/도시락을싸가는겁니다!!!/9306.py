# 9306: Practice: Roll Call
import sys
input = sys.stdin.readline
def solution():
    t = int(input())
    for tc in range(1, t + 1):
        f = input().strip()
        l = input().strip()
        print(f'Case {tc}: {l}, {f}')
solution()