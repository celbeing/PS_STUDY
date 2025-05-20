#2618 경찰차
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
W = int(input())
case = [[1,1]]+[list(map(int,input().split())) for _ in range(W)]
dist = [[-1 for _ in range(W+1)] for _ in range(W+1)]

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def dp(i,j):
    if i == W or j == W:
        return 0
    if dist[i][j] == -1:
        dist_i,dist_j,next = 0,0,max(i,j)+1
        if i == 0:
            dist_i = distance(case[next],[1,1])
        else:
            dist_i = distance(case[next],case[i])
        if j == 0:
            dist_j = distance(case[next],[N,N])
        else:
            dist_j = distance(case[next],case[j])
        dist_i += dp(next,j)
        dist_j += dp(i,next)
        if dist_i < dist_j:
            dist[i][j] = dist_i
        else:
            dist[i][j] = dist_j
    return dist[i][j]

def path(i,j):
    if i == W or j == W:
        return
    dist_i,dist_j,next = 0,0,max(i,j)+1
    if i == 0:
        dist_i = distance(case[next],[1,1])
    else:
        dist_i = distance(case[next],case[i])
    if j == 0:
        dist_j = distance(case[next],[N,N])
    else:
        dist_j = distance(case[next],case[j])
    if dist[next][j] + dist_i < dist[i][next] + dist_j:
        print(1)
        path(next,j)
    else:
        print(2)
        path(i,next)

dp(0,0)
print(dist[0][0])
path(0,0)