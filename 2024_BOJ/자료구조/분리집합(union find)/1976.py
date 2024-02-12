#1976: 여행 가자
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
union = [i for i in range(N+1)]

def head(k):
    while union[k] != k:
        k = union[k]
    return k

for i in range(N):
    link = list(map(int,input().split()))
    for j in range(N):
        if link[j] == 1:
            I = head(i+1)
            J = head(j+1)
            union[J] = I

route = list(map(int,input().split()))
p = head(route[0])
for a in route:
    if head(a) != p:
        print("NO")
        exit()
print("YES")