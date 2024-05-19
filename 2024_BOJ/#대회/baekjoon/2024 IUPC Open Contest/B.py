N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
if A[-1] < 0: print(0)
else:
    score = 0
    for i in range(1,M+1):
        if A[-i] < 0 or i*2 > N+1: break
        score += A[-i]
    print(score)