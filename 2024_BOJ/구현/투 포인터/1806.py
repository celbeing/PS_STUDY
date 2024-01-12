#1806: 부분합
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
arr.append(0)

a,b = 0,0
sum = arr[0]
result = N+1

while b < N:
    if sum < S:
        b+=1
        sum+=arr[b]
    else:
        if b > a:
            if b-a+1 < result:
                result = b-a+1
            sum-=arr[a]
            a+=1
        else:
            result = 1
            break
if result > N:
    print(0)
else:
    print(result)