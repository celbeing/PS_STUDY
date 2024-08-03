#2193: 이친수
N = int(input())
dp0 = [0]*(N+1)
dp1 = [0]*(N+1)
dp1[1] = 1
for i in range(2,N+1):
    dp0[i] = dp0[i-1]+dp1[i-1]
    dp1[i] = dp0[i-1]
print(dp0[N]+dp1[N])