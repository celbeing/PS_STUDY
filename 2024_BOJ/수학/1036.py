#1036: 36진수
import sys
input = sys.stdin.readline

N = int(input())
count = [[0 for _ in range(36)] for _ in range(50)]
base = list(map(str,"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
for _ in range(N):
    num = list(map(str, input().rstrip()))
    for i in range(0, len(num)):
        a = base.index(num[-1-i])
        count[i][a]+=1

K = int(input())

b = 1
for i in range(1,50):
    b *= 36
    for j in range(36):
        count[0][j] += count[i][j] * b

while K > 0:
    profit = 0
    index = -1
    for i in range(35):
        if count[0][i] * (35-i) > profit:
            profit = count[0][i] * (35 - i)
            index = i
    if profit == 0:
        break
    else:
        count[0][35] += count[0][index]
        count[0][index] = 0
        K -= 1

sum = 0
for i in range(36):
    sum += count[0][i] * i

result = []
while True:
    result.insert(0,base[sum%36])
    sum //= 36
    if sum == 0:
        break
print(''.join(result))