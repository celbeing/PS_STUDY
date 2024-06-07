# 9576: 책 나눠주기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def match(k):
    if visit[k]: return False
    visit[k] = True
    for t in graph[k]:
        if stud[t] == -1:
            stud[t] = k
            return True
    for t in graph[k]:
        if stud[t] >= 0 and match(stud[t]):
            stud[t] = k
            return True
    return False

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    count = 0

    stud = [-1]*(M+1)

    # 원하는 책 이어주기
    for m in range(1,M+1):
        a,b = map(int,input().split())
        for i in range(a,b+1):
            graph[i].append(m)

    # 매칭
    for i in range(1,N+1):
        visit = [False]*(N+1)
        if match(i): count += 1
        if count == M: break

    print(count)