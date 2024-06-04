#31713: 행운을 빌어요
import sys, math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    if A*3 <= B <= A*4:
        print(0)
    elif A*3 > B:
        print(A*3-B)
    elif A == 0:
        if B == 0:
            print(4)
        elif B == 1:
            print(3)
        elif B == 2:
            print(2)
        elif 3<=B<=4:
            print(1)
        elif B == 5:
            print(3)
        else:
            print(int(math.ceil(B/4)-A))
    elif B == 5:
        print(2)
    else:
        print(int(math.ceil(B/4)-A))