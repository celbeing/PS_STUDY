#1107: 리모컨
N = int(input())
M = int(input())
if M == 0:
    button = []
else:
    button = list(map(int,input().split()))
case = []
lower,upper = 0,0
for i in range(N, -1, -1):
    lower = 0
    if i == 0:
        lower += 1
    k = i
    while k > 0:
        if k%10 in button:
            break
        k //= 10
        lower += 1
    else:
        lower += N-i
        break

for i in range(N+1,1000001):
    upper = 0
    k = i
    while k > 0:
        if k%10 in button:
            break
        k //= 10
        upper += 1
    else:
        upper += i-N
        break

if N > 100:
    upper = min(upper, N-100)
else:
    lower = min(lower, 100-N)

print(min(lower,upper))