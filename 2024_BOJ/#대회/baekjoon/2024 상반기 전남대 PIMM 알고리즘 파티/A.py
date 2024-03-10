#A: 시계탑
import sys
input = sys.stdin.readline
M = int(input())
result = 0
if M > 30:
    result += 15
    M -= 30
    result += M/2*3
else:
    result = M / 2
print("{:.1f}".format(result))