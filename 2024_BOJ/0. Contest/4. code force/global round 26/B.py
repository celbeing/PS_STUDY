import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x = list(input().rstrip())
    n = len(x)
    flag = True
    if int(x[0]) == 1 and 0<=int(x[-1])<=8:
        for i in range(1,n-1):
            if 1<=int(x[i])<=9:
                continue
            else:
                flag = False
                break
    else:
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")