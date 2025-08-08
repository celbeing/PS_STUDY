# 1837: 암호제작
import sys
input = sys.stdin.readline
def solution():
    p, k = map(int, input().split())
    for i in range(2, k):
        if p % i: continue
        else:
            print(f'BAD {i}')
            return
    print('GOOD')
solution()