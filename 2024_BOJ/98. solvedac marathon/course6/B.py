N,K,A,B = map(int,input().split())
day = 1
catnip = [K]*N
water = 0
while True:
    for i in range(water,water+A):
        catnip[i] += B
    water += A
    water %= N
    for i in range(N):
        catnip[i] -= 1
        if catnip[i] == 0:
            print(day)
            exit()
    day += 1