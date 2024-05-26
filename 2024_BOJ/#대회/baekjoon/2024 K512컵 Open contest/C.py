N = int(input())
S = list(input().rstrip())

sum = [i for i in range(N+1)]
sumsum = [0]*(N+1)
for i in range(1,N+1):
    sumsum[i] = sum[i] + sumsum[i-1]
sumsumsum = [0]*(N+1)
for i in range(1,N+1):
    sumsumsum[i] = sumsum[i] + sumsumsum[i-1]

result = 0
count = 0
for k in S:
    if k == '2':
        count += 1
    else:
        result += sumsumsum[count]
        count = 0
print(result+sumsumsum[count])