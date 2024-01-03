#1406: 에디터
#이 문제는 연결리스트로 푸는 것이 정석임
import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

N = int(input())
for n in range(N):
    o = list(input().split())
    if o[0] == "L" and left:
        right.append(left.pop())
    elif o[0] == "D" and right:
        left.append(right.pop())
    elif o[0] == "B" and left:
        left.pop()
    elif o[0] == "P":
        left.append(o[1])
left.extend(reversed(right))
print(''.join(left))