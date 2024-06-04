import sys
input = sys.stdin.readline
N = int(input())
couple = {}
for _ in range(N):
    p,s = map(str,input().split())
    if s == "-": continue
    if s in couple:
        couple[s].append(p)
    else:
        couple[s] = []
        couple[s].append(p)
count = 0
result = []
for ring in couple:
    if len(couple[ring]) == 2:
        count += 1
        result.append(couple[ring])
print(count)
for k in result:
    print(*k)