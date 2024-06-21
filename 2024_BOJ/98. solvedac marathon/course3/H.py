import sys
from collections import deque
input = sys.stdin.readline

def sieve():
    prime = []
    s = [1]*10001
    s[0] = 0
    s[1] = 0
    for i in range(2,10001):
        if s[i]:
            prime.append(i)
            if i > 1000: link[i] = []
            for j in range(i**2,10001,i):
                s[j] = 0
    return prime[168:]

link = dict()
prime = sieve()
for p in prime:
    for i in range(1,10-p%10):
        if p+i in prime:
            link[p].append(p+i)
            link[p+i].append(p)
    for i in range(1,10-p//10%10):
        if p+i*10 in prime:
            link[p].append(p+i*10)
            link[p+i*10].append(p)
    for i in range(1,10-p//100%10):
        if p+i*100 in prime:
            link[p].append(p+i*100)
            link[p+i*100].append(p)
    for i in range(1,10-p//1000):
        if p+i*1000 in prime:
            link[p].append(p+i*1000)
            link[p+i*1000].append(p)

def find():
    s,t = map(int,input().split())
    bfs = deque([s])
    visit = dict()
    step = 0
    for p in prime:
        visit[p] = True
    while bfs:
        k = len(bfs)
        for _ in range(k):
            now = bfs.popleft()
            if now == t:
                print(step)
                return
            for next in link[now]:
                if visit[next]:
                    bfs.append(next)
                    visit[next] = False
        step += 1
    print("Impossible")
    return

T = int(input())
for _ in range(T):
    find()