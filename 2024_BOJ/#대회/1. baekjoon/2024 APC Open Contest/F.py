N = int(input())
A = list(map(int,input().split()))
print(N//2)
t = 5000*(N//2)
for i in range(N//2):
    A[i] += t
    A[-(i+1)] -= t
    print(*A)
    t -= 5000