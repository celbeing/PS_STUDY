S = input()
T = input()
cnt = 0
if S == T:
    print(0)
else:
    n = min(len(S), len(T))
    while cnt < n:
        if S[cnt] == T[cnt]:
            pass
        else:
            break

        cnt += 1
    print(cnt + 1)