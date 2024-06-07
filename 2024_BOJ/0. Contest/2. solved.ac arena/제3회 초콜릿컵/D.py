#D: 삼각 초콜릿 포장 (Sweet)
import sys
input = sys.stdin.readline
N = int(input())
chocolates = [list(input().rstrip()) for _ in range(N)]
check = [[False for j in range(i)] for i in range(1, N + 1)]
flag = True
for i in range(1,N+1):
    for j in range(i):
        if check[i-1][j]: continue
        if chocolates[i-1][j] == "R":
            if i == N:
                flag = False
                break
            if chocolates[i][j] == chocolates[i][j+1] == "R" and not(check[i][j]):
                check[i][j] = True
                check[i][j+1] = True
                check[i-1][j] = True
            else:
                flag = False
                break
        else:
            if i == N or j == i-1:
                flag = False
                break
            if chocolates[i-1][j+1] == chocolates[i][j+1] == "B" and not(check[i-1][j+1]):
                check[i-1][j+1] = True
                check[i-1][j] = True
                check[i][j+1] = True
            else:
                flag = False
                break
if flag:
    print(1)
else:
    print(0)