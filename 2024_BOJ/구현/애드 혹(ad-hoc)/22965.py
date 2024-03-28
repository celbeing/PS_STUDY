#22965: k개의 부분 배열
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
flag1 = False
flag2 = False
for i in range(1,N):
    if A[i]<A[i-1]:
        if flag1:
            flag2 = True
            break
        else:
            if A[-1] < A[0]:
                flag1 = True
            else:
                flag1 = True
                flag2 = True
                break
if flag1:
    if flag2:
        print(3)
    else:
        print(2)
else:
    print(1)