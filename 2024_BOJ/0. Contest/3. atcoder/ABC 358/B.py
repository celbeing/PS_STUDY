import sys
input = sys.stdin.readline
N,A = map(int,input().split())
T = list(map(int,input().split()))
time = 0
wait = [0]*N
for i in range(N):
    if time < T[i]: time = T[i]
    wait[i] = time+A
    time += A
print(*wait)
