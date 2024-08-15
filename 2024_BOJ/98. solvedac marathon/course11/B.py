#17211: 좋은 날 싫은 날
import sys
input = sys.stdin.readline
N,feel = map(int,input().split())
posb = list(map(float, input().split()))
good = 1-feel
bad = 1-good
for _ in range(N):
    next_good = good*posb[0]+bad*posb[2]
    next_bad = good*posb[1]+bad*posb[3]
    good = next_good
    bad = next_bad
print(int(good*1000))
print(int(bad*1000))