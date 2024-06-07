#A: 그게 무슨 코드니..
import sys
input = sys.stdin.readline
S = list(input().rstrip())
if len(S) > 2 and S[0] == "\"" and S[-1] == "\"":
    print(''.join(S[1:-1]))
else:
    print("CE")