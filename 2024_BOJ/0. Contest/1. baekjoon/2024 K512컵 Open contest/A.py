N,M = map(int,input().split())
score = sum(list(map(int, input().split())))
m = list(map(int,input().split()))
for k in m:
    if k > 0: score*=k
print(score)