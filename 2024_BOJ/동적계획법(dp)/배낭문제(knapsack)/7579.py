#7579: 앱
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
mem = list(map(int,input().split()))
cos = list(map(int,input().split()))
result = sys.maxsize

#k[a][c] = a번째 앱까지 비용 c로 확보하는 최대 메모리
k=[[0 for _ in range(10001)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(sum(cos)+1):
        if j - cos[i-1] >= 0:
            k[i][j] = max(k[i][j],k[i-1][j-cos[i-1]]+mem[i-1])
        k[i][j] = max(k[i][j], k[i-1][j])
        if k[i][j] >= M:
            if result > j:
                result = j
print(result)