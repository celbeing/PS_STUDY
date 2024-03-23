A,B = map(int,input().split())
C = int(input())
R = A+B-C-C
if R < 0:
    print(A+B)
else:
    print(R)