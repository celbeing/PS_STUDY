#4386: 별자리 만들기
import sys
input = sys.stdin.readline
n = int(input())
star = [tuple(map(float,input().split())) for _ in range(n)]
root = [i for i in range(n)]

def find(k, r):
    while k != r[k]: k = r[k]
    return k

line = []
for i in range(n-1):
    for j in range(i+1,n):
        line.append(((star[i][0]-star[j][0])**2+(star[i][1]-star[j][1])**2,i,j))
line.sort(reverse=True)

count = 0
length = 0

while line and count < n-1:
    l,a,b = line.pop()
    root_a = find(a,root)
    root_b = find(b,root)
    if root_a == root_b: continue
    else:
        count += 1
        length += l**0.5
        if root_a < root_b:
            root[root_b] = root_a
        else:
            root[root_a] = root_b

print(length)