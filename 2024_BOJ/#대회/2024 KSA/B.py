import sys
input = sys.stdin.readline
X = list(input().rstrip())
ksa = ['K','S','A']
state = [0,1,2]
remain = [0]*3
isK = False
if len(X) == 1:
    if X[0] == "K":
        print(0)
        exit()
    else:
        print(2)
        exit()
elif len(X) == 2:
    if X[1] == "K":
        print(2)
        exit()
    elif X == ['A','A']:
        print(4)
        exit()

for i in range(len(X)):
    if not isK:
        if X[i] == "K":
            isK = True

    if X[i] == ksa[state[0]]:
        remain[0] += 1
        state[0] += 1
        state[0] %= 3
    if X[i] == ksa[state[1]]:
        remain[1] += 1
        state[1] += 1
        state[1] %= 3
    if X[i] == ksa[state[2]]:
        remain[2] += 1
        state[2] += 1
        state[2] %= 3

result = [0,0,0]
result[0] = (len(X)-remain[0])*2
if len(X) > 2:
result[1] =

if isK:
    print(min(remain)*2)
else:
    print(min(remain)*2-2)