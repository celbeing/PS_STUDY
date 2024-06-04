import sys
from collections import deque
input = sys.stdin.readline
N,K,M = map(int,input().split())
letters = list("-[]abcdefghijklmnopqrstuvwxyz.")
d = {}
for i in range(30):
    d[letters[i]] = i
corpus = [[[0,i] for i in range(30)] for _ in range(30)]
for _ in range(N):
    train = list(input().rstrip())
    i = 0
    while True:
        if train[i] == ']': break
        corpus[d[train[i]]][d[train[i+1]]][0] += 1
        i += 1
result = {}
for i in range(30):
    corpus[i].sort()
    high = 0
    index = 0
    for j in range(30):
        if corpus[i][j][0] > high:
            high = corpus[i][j][0]
            index = corpus[i][j][1]
    result[letters[i]] = letters[index]
result["]"] = "."
result["."] = "."
create = "["
loop = ""
visit = [0]*30
visit[1] = 1
fin = False
for i in range(1, K+M-1):
    if visit[d[result[create[-1]]]]:
        break
    else:
        visit[d[result[create[-1]]]] = 1
    create += result[create[-1]]
    if create[-1] == ".":
        fin = True
        create += "."*(K+M-i)
        break
if fin: print(create[K-1:K+M-1])
else:
    loop += result[create[-1]]
    while not(loop[0] == result[loop[-1]]):
        loop += result[loop[-1]]
    while len(create) < K+M:
        create += loop
    print(create[K-1:K+M-1])