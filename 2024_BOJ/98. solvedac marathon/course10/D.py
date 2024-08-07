#27172: 수 나누기 게임
import sys
input = sys.stdin.readline
N = int(input())
x = list(map(int,input().split()))
card = [0]*1000001
for c in x: card[c] = 1
score = [0]*1000001
for i in x:
    for j in range(i*2,1000001,i):
        if card[j]:
            score[i] += 1
            score[j] -= 1
res = [0]*N
for i in range(N):
    res[i] = score[x[i]]
print(*res)