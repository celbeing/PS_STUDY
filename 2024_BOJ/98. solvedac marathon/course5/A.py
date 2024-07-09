N = int(input())
for i in range(64,0,-1):
    if N&1:
        print(i)
        break
    else:
        N//=2