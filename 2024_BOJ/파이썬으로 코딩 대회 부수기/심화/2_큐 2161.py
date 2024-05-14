from collections import deque
N = int(input())
card = deque()
for i in range(1,N+1):
    card.append(i)

throw = []
for i in range(N-1):
    throw.append(card.popleft())
    card.append(card.popleft())
throw.append(card[0])
print(*throw)

