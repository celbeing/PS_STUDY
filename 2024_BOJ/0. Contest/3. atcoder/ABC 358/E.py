import sys
input = sys.stdin.readline
div = 998244353
perm = [[0]*1001 for _ in range(1001)]
for i in range(1,1001):
    perm[i][1] = i
    for j in range(2,i):
        perm[i][i-j] = perm[i][
K = int(input())
C = list(map(int,input().split()))
total = 0
nowC = [0]*26
result = 0
for i in range(1,K+1):
    for j in range(26):
        if C[j] >= i:
            nowC[j] += 1
            total += 1
    if total < i: break
    mult = [k for k in range(total-i+1,total+1)]
    for j in range(26):
        if nowC[j]:
            index = len(mult)-1
            for k in range(1,nowC[j]+1):
                while mult[index] % k > 0: index -= 1
                mult[index] //= k
    res = 1
    for t in mult:
        res *= t
        if res >= div: res %= div
    result += res
print(result)