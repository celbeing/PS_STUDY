n = int(input())
stone = list(map(int, input().split()))
left = []
right = []
now = stone[0]
count = 1
for i in range(1, n):
    if now == stone[i]:
        count += 1
    else:
        if now & 1:
            left.append(count)
            right.append(-count)
            now = 2
        else:
            left.append(-count)
            right.append(count)
            now = 1
        count = 1
if now & 1:
    left.append(count)
    right.append(-count)
else:
    left.append(-count)
    right.append(count)

high = 0
sum = 0
for k in left:
    if sum + k < 0:
        sum = 0
    else:
        sum += k
    high = max(high, sum)
sum = 0
for k in right:
    if sum + k < 0:
        sum = 0
    else:
        sum += k
    high = max(high, sum)
print(high)