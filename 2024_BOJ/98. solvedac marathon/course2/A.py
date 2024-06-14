import sys
input = sys.stdin.readline

while True:
    s = list(input().split())
    if s == ["*"]: break

    t = s[0][0].lower()
    flag = False
    for i in range(1,len(s)):
        if flag: break
        if s[i][0].lower() == t: continue
        else:
            flag = True
    if flag: print("N")
    else: print("Y")