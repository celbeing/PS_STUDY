S = list(input())
R,M = -1,-1
for i in range(3):
    if S[i] == "R": R = i
    elif S[i] == "M": M = i
if R < M: print("Yes")
else: print("No")