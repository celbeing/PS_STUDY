#28417: 스케이트보드
import sys
input = sys.stdin.readline
N = int(input())
record = 0
run = []
trick = []
for i in range(N):
    score = list(map(int,input().split()))
    run = max(score[0:2])
    trick = sorted(score[2:])
    high = run + trick[3] + trick[4]
    if high > record:
        record = high
print(record)