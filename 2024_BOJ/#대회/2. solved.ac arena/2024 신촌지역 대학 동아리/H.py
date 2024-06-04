# H: 신촌 통폐합 계획
import sys
input = sys.stdin.readline
N = int(input())
univ = ['']+[input().rstrip() for _ in range(N)]
root = [i for i in range(N + 1)]
next = [i for i in range(N + 1)]
leaf = [i for i in range(N + 1)]
k = 0
for _ in range(N-1):
    i,j = map(int,input().split())
    k = i
    root[j] = leaf[i]
    next[leaf[i]] = j
    leaf[i] = leaf[j]
for i in range(N):
    print(univ[k], end='')
    k = next[k]