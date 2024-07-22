import sys
input = sys.stdin.readline
N,K = map(int,input().split())
w = sorted(list(map(int,input().split())))
count = 0
s,e = 0,N-1
while s < e:
    if w[s]+w[e] <= K:
        count += 1
        s += 1
        e -= 1
    else:
        e -= 1
print(count)