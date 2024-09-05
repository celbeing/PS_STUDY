#4929: 수열 걷기
import sys
input = sys.stdin.readline
def solution():
    while True:
        A = list(map(int,input().split()))
        if A == [0]: return
        B = list(map(int,input().split()))
        a,b = 1,1
        total = 0
        sa,sb = 0,0
        while a <= A[0] and b <= B[0]:
            if A[a] < B[b]:
                sa += A[a]
                a += 1
            elif A[a] > B[b]:
                sb += B[b]
                b += 1
            else:
                total += max(sa,sb)+A[a]
                sa,sb = 0,0
                a += 1
                b += 1
        while a <= A[0]:
            sa += A[a]
            a += 1
        while b <= B[0]:
            sb += B[b]
            b += 1
        total += max(sa,sb)
        print(total)
solution()