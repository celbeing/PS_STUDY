N = int(input())
result = 0
for i in range(1,N+1):
    result += (N//i)*i
print(result)