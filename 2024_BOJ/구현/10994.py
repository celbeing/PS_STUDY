#10994: 별 찍기 - 19
N = int(input())
k = N * 4 - 3
star = [[' '] * k for _ in range(k)]
for i in range(N):
    t = i * 2
    for j in range(t, t+k):
        star[t][j] = '*'
        star[t+k-1][j] = '*'
    for j in range(1,k-1):
        star[t+j][t] = '*'
        star[t+j][t+k-1] = '*'
    k -= 4
for a in star:
    print(''.join(a))