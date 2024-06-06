# 11899: 괄호 끼워넣기
import sys
input = sys.stdin.readline
s = list(input().rstrip())
t = 0
result = 0
for i in s:
    if i == ')': t -= 1
    else: t += 1
    if t < 0:
        result += 1
        t += 1
print(result+t)