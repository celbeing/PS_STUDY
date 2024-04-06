#1653: 양팔 저울
import sys
input = sys.stdin.readline
n = int(input())
W = list(map(int,input().split()))
k = int(input())

def calc(w):
    r = 0
    for i in range(1,6):
        r += i*(w%10)
        w //= 10
    return r

def reverse(w):
    r = 0
    for _ in range(1,6):
        r *= 10
        r += w%10
        w //= 10
    return r

def check(a,b):
    c = [0]*10
    while a > 0:
        c[a%10] += 1
        a //= 10
    while b > 0:
        c[b%10] += 1
        b //= 10

    for i in range(1,10):
        if c[i] > 1: return False
        elif c[i] == 1:
            if i not in W: return False

    return True

memo = [[] for _ in range(116)]
solution = [0]
for i in range(1,98766):
    if check(i,0): memo[calc(i)].append(i)
for n in range(1,116):
    if memo[n]:
        for i in range(len(memo[n])-1):
            for j in range(i+1,len(memo[n])):
                if check(memo[n][i],memo[n][j]):
                    solution.append(memo[n][i]*100000+reverse(memo[n][j]))
                    solution.append(memo[n][j]*100000+reverse(memo[n][i]))
solution.sort()
if k >= len(solution): print(solution[-1])
else: print(solution[k])