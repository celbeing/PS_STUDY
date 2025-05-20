# 27977: 킥보드로 등교하기
import sys
input = sys.stdin.readline
def solution():
    l, n, k = map(int, input().split())
    a = list(map(int, input().split()))
    def check(b):
        count = 0
        dist = b
        last = 0
        for d in a:
            if d > dist:
                dist = last + b
                if d <= dist: count += 1
                else:
                    count = k + 1
                    break
            last = d
        if dist < l:
            dist = last + b
            count += 1
            if dist < l:
                count = k + 1
        return count
    s, e = 1, 200000
    while s < e:
        m = (s + e) // 2
        if check(m) > k:
            s = m + 1
        else:
            e = m
    print(s)
solution()