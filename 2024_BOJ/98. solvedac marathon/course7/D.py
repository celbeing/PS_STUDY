import sys
input = sys.stdin.readline

def time(t):
    h,m = map(int,t.split(":"))
    return h*60+m

S,E,Q = map(str,input().split())
S = time(S)
E = time(E)
Q = time(Q)

count = 0
check = {}
while True:
    i = input().rstrip()
    if i == "": break

    t,n = i.split()
    t = time(t)
    if t<=S:
        if n in check:
            if check[n] == 2:
                check[n] += 1
                count += 1
        else:
            check[n] = 1
    elif E<=t<=Q:
        if n in check:
            if check[n] == 1:
                check[n] += 2
                count += 1
        else:
            check[n] = 2
print(count)