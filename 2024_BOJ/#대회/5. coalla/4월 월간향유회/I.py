# 30054: 웨이팅
import sys
input = sys.stdin.readline
N = int(input())
time = 0
wait = [-1]*200001 # 예약시간에 저장
rsv = []
for _ in range(N):
    t1,t2 = map(int,input().split())
    if t1 >= t2: wait[t1] = -t2-1
    rsv.append((t2, t1))
rsv.sort()
queued = 0 # 대기열 끝
enter = 0  # 다음 입장
for t in range(1,200001):
    # 대기열에 추가
    while queued < N and rsv[queued][0] == t: queued += 1
    while queued > enter and wait[rsv[enter][1]] >= 0: enter += 1

    # 한 명 입장
    if wait[t] < -1: wait[t] += t+1
    elif queued > enter:
        wait[rsv[enter][1]] = t-rsv[enter][0]
        enter += 1

long = 0
for k in wait:
    if long < k:
        long = k
print(long)