#10867: 중복 빼고 정렬하기
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
d = dict()
for a in arr:
    d[a] = 1
print(*sorted(d))