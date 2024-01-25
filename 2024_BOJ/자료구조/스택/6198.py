#6198: 옥상 정원 꾸미기
import sys
input = sys.stdin.readline
N = int(input())
building = [int(input()) for _ in range(N)]
building.append(1e9)
benchmark = -N
sight = []
for i in range(N+1):
    if len(sight) == 0:
        sight.append(i)
    else:
        while len(sight) > 0 and building[sight[-1]] <= building[i]:
            k = sight.pop()
            benchmark += i-k
        sight.append(i)
print(benchmark)