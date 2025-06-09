# 1471: 사탕 돌리기
import sys
input = sys.stdin.readline
n = int(input())
edge = [0] * (n + 1)
dec = [0] * 7
dec[0] = 0
count = 0
for i in range(1, n + 1):
    count += 1
    for j in range(6):
        dec[j] += 1
        if dec[j] == 10:
            count -= 9
            dec[j] = 0
        else:
            break
    if (i + count) % n == 0:
        edge[i] = n
    else:
        edge[i] = (i + count) % n
print(edge)