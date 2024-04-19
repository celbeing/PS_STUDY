#17178: 줄서기
import sys
from collections import deque
from heapq import heappush,heappop
input = sys.stdin.readline
N = int(input())
ticket = deque([])
order = []
waiting = deque([])
for _ in range(N):
    line = list(input().split())
    for fan in line:
        a,b = fan.split('-')
        ticket.append((ord(a)-ord('A'))*1000+int(b))
        heappush(order,ticket[-1])
while order:
    if ticket and ticket[0] == order[0]:
        heappop(order)
        ticket.popleft()
    elif waiting and waiting[0] == order[0]:
        heappop(order)
        waiting.popleft()
    elif ticket:
        waiting.appendleft(ticket.popleft())
    else:
        print("BAD")
        break
else:
    print("GOOD")