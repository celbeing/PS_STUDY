#1107: 리모컨
N = int(input())
M = int(input())
if M == 0:
    button = []
else:
    button = list(map(int,input().split()))
result = abs(N - 100)

l,u = 1e9,1e9

for i in range(N, 0, -1):
    lower = 0
    if i == 0:
        lower += 1
    k = i
    while k > 0:
        if k % 10 in button:
            break
        k //= 10
        lower += 1
    else:
        lower += N-i
        l = lower
        break
if not(0 in button) and l > N+1:
    l = N+1

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
        u = upper
        break

if result > l:
    result = l
if result > u:
    result = u

print(result)