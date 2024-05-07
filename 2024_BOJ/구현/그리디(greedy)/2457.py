# 2457: 공주님의 정원
import sys
input = sys.stdin.readline
N = int(input())
flower = []
for _ in range(N):
    a,b,c,d = map(int,input().split())
    flower.append((a*100+b,c*100+d))
flower.sort()
end = 301
cand = -1
count = 0
for i in range(N):
    if end > 1131: break
    if flower[i][0] <= end:
        if flower[i][1] > 1131:
            count += 1
            end = flower[i][1]
            break
        if flower[i][1] > cand: cand = flower[i][1]
    else:
        if cand < flower[i][0]: break
        end = cand
        cand = flower[i][1]
        count += 1
        if cand > 1131:
            end = cand
            count += 1
            break
if end > 1131:
    print(count)
else:
    print(0)