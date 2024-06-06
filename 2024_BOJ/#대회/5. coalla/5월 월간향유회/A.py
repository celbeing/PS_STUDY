import sys
input = sys.stdin.readline

case = 1
while True:
    L,P,V = map(int,input().split())
    if L == 0: break
    r = V//P*L + min(V%P,L)
    print("Case %d: %d"%(case,r))
    case += 1