#25979: 시간 구간 다중 업데이트 최대 합
import sys
input = sys.stdin.readline
def second(s):
    hs, ms, ss = map(int, s.split(':'))
    s = (hs*60+ms)*60+ss
    return s

def solution():
    N = int(input())
    time = [list(map(str, input().split()))[1:] for _ in range(N - 1)]
    prefix = [0] * 86401
    start = []
    end = []
    for i in range(N - 1):
        start.append(second(time[i][0]))
        end.append(second(time[i][1]))
    start.sort()
    end.sort()
    start.append(-1)
    end.append(-1)
    s, e = 0, 0
    cnt = 0
    for i in range(86400):
        while i == start[s]:
            cnt += 1
            s += 1
        while i == end[e]:
            cnt -= 1
            e += 1
        prefix[i] += cnt
        prefix[i + 1] = prefix[i]
    prefix.append(0)
    term = second(input().rstrip()[2:])
    res = 0
    for i in range(86401 - term):
        if res < prefix[term + i - 1] - prefix[i - 1]:
            res = prefix[term + i - 1] - prefix[i - 1]
    print(res)
solution()