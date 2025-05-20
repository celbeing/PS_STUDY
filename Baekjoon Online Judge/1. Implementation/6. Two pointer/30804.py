# 30804: 과일 탕후루
N = int(input())
S = list(map(int,input().split()))
i = [[0,0,0],[0,0,0]]
k = 1
l = 0
i[0][0] = S[0]
while k < N and S[k] == i[0][0]:
    k += 1
if k < N:
    i[1][0] = S[k]
    i[1][1] = k
    i[1][2] = k
    i[0][2] = k-1
else:
    print(N)
    exit()
k += 1
while k < N:
    if S[k] == i[0][0]:
        i[0][2] = k
    elif S[k] == i[1][0]:
        i[1][2] = k
    else:
        l = max(k-min(i[0][1],i[1][1]),l)
        if i[0][2] < i[1][2]:
            i[1][1] = i[0][2]+1
            i[0][0] = S[k]
            i[0][1] = k
            i[0][2] = k
        else:
            i[0][1] = i[1][2]+1
            i[1][0] = S[k]
            i[1][1] = k
            i[1][2] = k
    k += 1

l = max(k-min(i[0][1],i[1][1]),l)
print(l)