#A: KSA 문자열
import sys
input = sys.stdin.readline
X = list(input().rstrip())
N = len(X)
ksa = ['K','S','A']
state = [0,1,2]
count = [0] * 3
result = [0]*3
firstK = -1

for i in range(N):
    if X[i] == 'K' and firstK == -1:
        firstK = i
    if X[i] == ksa[state[0]]:
        count[0] += 1
        state[0] += 1
        state[0] %= 3
    if X[i] == ksa[state[1]]:
        count[1] += 1
        state[1] += 1
        state[1] %= 3
    if X[i] == ksa[state[2]]:
        count[2] += 1
        state[2] += 1
        state[2] %= 3

if firstK == 0:
    print((N - count[0]) * 2)
else:
    result[0] = (N - count[0]) * 2
    if count[1] == N:
        result[1] = 2
    else:
        result[1] = (N - count[1]) * 2
    if count[2] == N:
        result[2] = 2
    elif count[2] == N - 1:
        result[2] = 4
    else:
        result[2] = (N - count[2]) * 2
    print(min(result))

'''
result[0] = (N - count[0]) * 2
if N > 2:
    result[1] = (N - count[1]) * 2
    if count[1] == N:
        result[1] += 2
    if N == 3:
        result[2] = (N - count[2] + 1)*2
    else:
        result[2] = (N - count[2]) * 2
        if count[2] == N:
            result[2] += 2
else:
    if count[1] == 2:
        result[1] = 2
    elif count[1] == 1:
        result[1] = 2
    else:
        result[1] = 2

    if count[2] == 2:
        result[2] = 2
    elif count[2] == 1:
        result[2] = 4
    else:
        result[2] = 2

print(min(result))
'''