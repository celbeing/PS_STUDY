t = 0
while True:
    n = list(map(int,input().split()))[1:]
    if n == []: break
    t += 1
    if len(n)&1:
        print("Case {}: {}".format(t,n[len(n)//2]/1))
    else:
        print("Case {}: {}".format(t, (n[len(n) // 2] + n[len(n) // 2 - 1]) / 2))