# 카탈란 게임
import sys
input = sys.stdin.readline
N = int(input())
S = list(input().rstrip())
if N % 2 == 0:
    print("junhui")
    exit()

Sleft = S[:N-1]
Sright = S[1:]

for i in range(N//2):
    if Sleft[i] == '(' and Sleft[N-i-2] == ')':
        check = 0
        for j in range(i, N-i-1):
            if Sleft[j] == '(':
                check += 1
            else:
                check -= 1
            if check < 0:
                break
        if check == 0:
            print("jimin")
            exit()
    if Sright[i] == '(' and Sright[N-i-2] == ')':
        check = 0
        for j in range(i, N-i-1):
            if Sright[j] == '(':
                check += 1
            else:
                check -= 1
            if check < 0:
                break
        if check == 0:
            print("jimin")
            exit()
print("junhui")