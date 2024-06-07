import sys
input = sys.stdin.readline
N = int(input())
join = []
result = []
for _ in range(N):
    d = list(input().split())
    if d[1] == "hewhak": continue
    if d[2] == "winner": continue
    if 0<int(d[3])<=3: continue
    join.append((int(d[4]),d[0]))
join.sort()
for i in range(10):
    if i == len(join): break
    result.append(join[i][1])
result.sort()
print(len(result))
for n in result:
    print(n)