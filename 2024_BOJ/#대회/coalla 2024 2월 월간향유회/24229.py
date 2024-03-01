#24229: 모두싸인 출근길
import sys
input = sys.stdin.readline
N = int(input())
board = sorted([tuple(map(int,input().split())) for _ in range(N)])

start = 0
end = 0
reach = 0

for i in range(N):
    s,e = board[i]
    if s <= end:
        if end < e:
            end = e
    else:
        jump = end * 2 - start
        if reach < jump:
            reach = jump
        if s <= reach:
            start = s
            end = e
        else:
            break

print(end)