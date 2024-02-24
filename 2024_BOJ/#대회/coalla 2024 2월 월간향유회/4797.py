#4797: 화학
import sys
from collections import deque
input = sys.stdin.readline
raw = deque(list(input().rstrip()))
part = []
atom = dict()
stack = deque([])
while raw:
    now = raw.popleft()
    if now == "(" or now == ")":
        part.append(now)

        #괄호 끝나고 숫자 끝날 때 까지 확인