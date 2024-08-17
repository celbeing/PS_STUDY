#30047: 함수 문자열
import sys
input = sys.stdin.readline
S = list(input().rstrip())
eval = []
while S:
    n = S.pop()
    if n == "x":
        eval.append(0)
    elif n == "g":
        if eval:
            eval[-1] += 1
        else:
            print(-1)
            exit()
    else:
        if len(eval) >= 2:
            f = min(eval.pop(),eval.pop())
            eval.append(f)
        else:
            print(-1)
            exit()
if len(eval) == 1:
    print(eval[0])
else: print(-1)