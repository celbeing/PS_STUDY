import sys
input = sys.stdin.readline

def bin(k):
    s,e = i,j+1
    while s < e:
        m = (s+e)//2
        if X[m] == k: return True
        elif X[m] < k: s = m+1
        else: e = m
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    X = sorted(list(map(int,input().split())))

    count = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if (X[i]+X[j])&1: continue
            if bin((X[i]+X[j])//2): count += 1

    print(count)