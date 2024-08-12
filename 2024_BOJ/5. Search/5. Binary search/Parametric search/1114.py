# 1114: 통나무 자르기
import sys
input = sys.stdin.readline
L,K,C = map(int,input().split())
S = set(map(int,input().split()))
S.add(L)
S = sorted(list(S),reverse = True)
for i in range(len(S)-1):
    S[i] -= S[i+1]

def log_count(l):
    logs = []
    i = 0
    while i < len(S):
        logs.append(0)
        while i < len(S) and logs[-1] <= l:
            if S[i] > l: return -1
            logs[-1] += S[i]
            i += 1
        if logs[-1] > l:
            logs[-1] -= S[i-1]
            i -= 1
    if len(logs) > C+1: return -1
    elif len(logs) == C+1: return logs[-1]
    else: return S[-1]

s,e = 0,L
long = L
first = L
while s < e:
    m = (s+e)//2
    t = log_count(m)
    if t == -1:
        s = m+1
    else:
        long = m
        first = t
        e = m
print(long,first)