#H: 신기한 미로의 가지
import sys
input = sys.stdin.readline
N = int(input())
check=[0]*(N+1)
check[1] = 1
cnt = 1
parent = [0]*(N+1)
leaves = [[] for _ in range(N+1)]
now = 1
while cnt < N:
    print("maze",flush=True)
    k = int(input())
    if check[k] == 1:
        if parent[k] == now:
            print("gaji ",now,flush=True)
            t = int(input())
            print("gaji ",parent[now],flush=True)
            t = int(input())
            now = parent[now]
        else:
            now = k
    else:
        leaves[now].append(k)
        check[k] = 1
        parent[k] = now
        now = k
        cnt += 1

print("answer",flush=True)
for i in range(1,N+1):
    for a in leaves[i]:
        print(i,a,flush=True)
exit()