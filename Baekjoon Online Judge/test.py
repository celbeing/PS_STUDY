import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    flag = 0
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            flag = 1
            a[j], a[j + 1] = a[j + 1], a[j]

    if flag == 0: break

print(i)