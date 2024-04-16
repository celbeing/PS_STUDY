#3770: 대한민국
import sys, math
input = sys.stdin.readline

def seg(tree, node, s, e, t):
    if s == e:
        tree[node] += 1
        if node % 2 == 0:
            return tree[node+1]
        else:
            return 0
    ret = 0
    m = (s+e)//2
    if t <= m:
        ret = seg(tree, node * 2, s, m, t)
    else:
        ret = seg(tree, node * 2 + 1, m + 1, e, t)

    tree[node] += 1
    if node % 2 == 0:
        return ret+tree[node+1]
    else:
        return ret

def solution():
    N,M,K = map(int,input().split())
    road = [tuple(map(int,input().split())) for _ in range(K)]
    road.sort()
    tree = [0]*(1<<math.ceil(math.log2(M))+1)
    crossed = 0
    for e,w in road:
        crossed += seg(tree, 1, 1, M, w)
    return crossed

T = int(input())
for t in range(1,T+1):
    print("Test case {}: {}".format(t,solution()))