#1007: 벡터 매칭
import sys, itertools
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    dot = [tuple(map(int,input().split())) for _ in range(N)]
    x_total,y_total = 0,0
    for x,y in dot:
        x_total += x
        y_total += y
    case = list(itertools.combinations(dot,N//2))
    result = 4e5
    for c in case:
        x_part,y_part = 0,0
        for x,y in c:
            x_part += x
            y_part += y
        vec = ((x_total - x_part*2)**2 + (y_total - y_part*2)**2)**0.5
        if result > vec:
            result = vec
    print(result)