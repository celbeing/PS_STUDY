import sys
from collections import deque

input = sys.stdin.readline
move = [[0,0],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
N,M,L,T,K = map(int,input().split())

# 지도 그리기
Map = [list(input().rstrip()) for _ in range(N)]

# 선생님 위치
teacher = []
for l in range(L):
    route = deque()
    for p in range(int(input())):
        route.append(list(map(int,input().split())))
        route[p][0]-=1
        route[p][1]-=1
    teacher.append(route)

if 200<max(N,M):
    print("SAD")
    exit()

# 파댕이의 탐색 정보(x,y,식당 도착여부)
nowq = deque([[0,0,0]])   # 현재t 탐색
next = deque()          # t+10 탐색
rest = deque()          # 식당에서 나온 파댕이

# 선생님께 걸렸는지 확인해보자~
def detected():
    avoid = set()
    for k in teacher:
        kx,ky = k[0][0],k[0][1]
        for d in move:
            avoid.add(tuple([kx+d[0],ky+d[1]]))
    return avoid

t = 5
danger = detected()

# 현재 탐색할 큐가 비었고 식당에서 나오는 파댕이도 없으면
# 모든 파댕이는 선생님께 들킨 것임
while nowq or rest:
    # 점심시간 지났나? > "SAD" 출력
    if t > T:
        print("SAD")
        exit()

    # 식당에서 출발할 파댕이가 있는가? > nowq 큐에 추가
    while rest and rest[0][2] <= t:
        nowq.append(rest.popleft())
        nowq[-1][2] = 1

    # 탐색할 파댕이의 위치 받기
    cor = nowq.popleft()
    x,y,r = cor[0],cor[1],cor[2]

    # 선생님께 걸렸나? > 탐색하지 않음
    if not((x==N-1 and y==M-1) or (x==0 and y==0)) and tuple([x,y]) in danger: continue

    # 파댕이 탐색 시작
    for d in move:
        dx = x+d[0]
        dy = y+d[1]
        if 0<=dx<N and 0<=dy<M and Map[dx][dy] == '.':
            # 식당에 처음 도착했나? > rest 큐에 추가
            if dx==N-1 and dy==M-1 and r == 0:
                rest.append([dx,dy,t+K])
            elif dx==dy==0 and r==1:
                print("YUMMY")
                exit()

            # 선생님께 걸리지 않았거나, 식당에 또 왔나? > next 큐에 추가
            elif not (tuple([dx,dy]) in danger) or (dx==N-1 and dy==M-1):
                if [dx,dy,r] in next: continue
                next.append([dx,dy,r])

    # 현재 큐가 비었으면 파댕이 큐 이사 시키기
    if not(nowq):
        # 선생님 이동
        for ts in teacher:
            ts.append(ts.popleft())
        danger = detected()

        # 파댕이 큐 이사
        while next:
            if tuple([next[0][0],next[0][1]]) in danger:
                next.popleft()
            else:
                nowq.append(next.popleft())

        # t 10 증가
        t+=10

print("SAD")