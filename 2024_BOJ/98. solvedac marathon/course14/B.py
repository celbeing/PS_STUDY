#12755: 수면 장애
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    i = 1
    k = 1
    while N > i*k*9:
        N -= i*k*9
        i *= 10
        k += 1
    print(str(i+(N-1)//k)[(N-1)%k])
solution()