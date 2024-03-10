#B: 초콜릿과 11과 팰린드롬
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(1,end='')
        for _ in range(N-2):
            print(2,end='')
        print(1)