import sys
input = sys.stdin.readline
N,M,T = map(int,input().split())
Q = list(map(int,input().split()))
P = int(input())-1
M -= Q[P]

# [][][만들어진 마릿수, 선택한 범위의 왼쪽 끝, 선택한 범위의 오른쪽 끝]
# knapsack = [[[0,P,P] for _ in range(N)] for _ in range(M+1)]
knapsack = [[] for _ in range(M+1)]
for i in range(N):
    knapsack[0]

#for m in range(1,M+1):
#    for n in range(N):

'''
for i in range(1<<N):
    if i & (1<<N-P):
        sum,tl,tr = 0,0,0
        for j in range(N):
            if i & (1<<j):
                sum+=Q[N-j-1]
        if sum==M:
            for j in range(N):
                if i & (1<<j):
                    tl = N-j
                    if tr == 0:
                        tr = N-j
            if (tl > P and tr-P <= T) or (tr < P and P-tl <= T) or (tr-tl+min(P-tl,tr-P) <= T):
                print("YES")
                exit()

print("NO")
'''