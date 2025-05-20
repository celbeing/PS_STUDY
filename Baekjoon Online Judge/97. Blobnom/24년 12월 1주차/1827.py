# 1827: 여행가이드
import sys
from math import sin, cos
from collections import deque
input = sys.stdin.readline

def get_time(time_n, cor_p, vel_p, dir_p, cor_g, vel_g):
    # time_n: 가이드 g가 승객 p를 향해 움직이기 시작한 시각
    # cor: 좌표 / vel: 속도 / dir: 방향
    x = cor_p[0] + cos(dir_p) * vel_p * time_n
    y = cor_p[1] + sin(dir_p) * vel_p * time_n
    a = vel_p ** 2 - vel_g ** 2
    b = (cos(dir_p) * (x - cor_g[0]) + sin(dir_p) * (y - cor_g[1])) * vel_p
    c = (x - cor_g[0]) ** 2 + (y - cor_g[1]) ** 2
    time = max(((b ** 2 - a * c) ** 0.5 - b) / a, (-b - (b ** 2 - a * c) ** 0.5) / a)
    return time, cor_p[0] + cos(dir_p) * vel_p * (time_n + time), cor_p[1] + sin(dir_p) * vel_p * (time_n + time)

def get_return(time, cor_p, vel_p, dir_p):
    x = cos(dir_p) * vel_p * time + cor_p[0]
    y = sin(dir_p) * vel_p * time + cor_p[1]
    return time + ((x ** 2 + y ** 2) ** 0.5 / vel_p)

def solution():
    n = int(input())
    velocity = float(input())
    people = [list(map(float, input().split())) for _ in range(n)]
    result = 1e6
    find = deque([(0, 0, 0, 0, 0)])
    while find:
        mask, time, gx, gy, p_arr = find.pop()
        if mask == (1 << n) - 1:
            if result > p_arr: result = p_arr
            continue
        for i in range(n):
            if mask & 1 << i: continue
            next_time, px, py = get_time(time, (people[i][0], people[i][1]), people[i][2], people[i][3], (gx, gy), velocity)
            new_time = next_time + time
            arr = get_return(new_time, (people[i][0], people[i][1]), people[i][2], people[i][3])
            find.append((mask | 1 << i, new_time, px, py, max(p_arr, arr)))
    print(round(result))
solution()