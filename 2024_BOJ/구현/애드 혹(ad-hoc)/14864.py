#14864: 줄서기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
number = [i for i in range(1,N+1)]
count = [0] * (N+1)
pair = []
for i in range(M):
    x,y = map(int,input().split())
    count[x] += 1
    pair.append([x,y])
result = []
for i in range(1, N+1):
    result.append(number[count[i]])
    del number[count[i]]
print(*result)

for x,y in pair:
    if result[x-1] < result[y-1]:
        print(-1)
        break
else:
    print(*result)