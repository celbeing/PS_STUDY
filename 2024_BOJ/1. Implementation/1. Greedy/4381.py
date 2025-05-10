# 4381: Bridge
import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    people = [int(input()) for _ in range(n)]
    people.sort()
    res = 0
    if n == 1:
        print(people[0])
        print(people[0])
        return
    step = people[0] + people[1] * 2
    k = 0
    if n & 1:
        k = people[2]
        del people[2]
    route = []
    for i in range(3, len(people), 2):
        route.append([people[0], people[1]])
        route.append([people[0]])
        route.append([people[i - 1], people[i]])
        route.append([people[1]])
        res += people[i] + step
    route.append([people[0], people[1]])
    res += people[1]
    if n & 1:
        route.append([people[0]])
        route.append([people[0], k])
        res += people[0] + k
    print(res)
    for r in route:
        print(*r)
solution()